#include <8052.h>
#include <stdlib.h>

unsigned char cnt = 0;
unsigned char ksr = 0;
unsigned char previousksr = 0;
unsigned char zero_duration = 0;
#define FOSC 1200000 // 12 MHz crystal
#define BAUD 9600    // 9600 baud rate

unsigned char random_num[4];                                             // 4位數的隨機數字
unsigned char gx_data[5];                                                // 猜測緩衝區
unsigned char tx_data[5];                                                // 傳送緩衝區
unsigned char rx_data[5];                                                // 接收緩衝區
unsigned int pos = 0;                                                    // 紀錄7seg顯示位置
unsigned int idx = 0;                                                    // 紀錄接收的數量
unsigned char seg[4] = {0b11111111, 0b11111111, 0b11111111, 0b11111111}; // 紀錄keypad讀取轉7 Segment
unsigned char AA = 0;
unsigned char BB = 0;

void displayDigit(unsigned char digit, unsigned char position) // display
{
    P2 = digit;
    P1 = 7 - position;
}

static unsigned char seven_segment[17] = {
    0b00111111, 0b00000110, 0b01011011, 0b01001111,
    0b01100110, 0b01101101, 0b01111101, 0b00000111,
    0b01111111, 0b01101111, 0b01110111, 0b01111100,
    0b00111001, 0b01011110, 0b01111001, 0b01110001,
    0b00000000};
unsigned char Digits[8];
unsigned char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};
void send(void)
{
    for (unsigned char i = 0; i < 4; i++)
    {
        Digits[i] = 0b00000000;
    }

    for (unsigned char i = 0; i < 5; i++)
    {
        TI = 0;
        SBUF = gx_data[i];
        while (!TI)
            ;
    }
}
void txsend(void)
{
    for (int i = 0; i < 5; i++)
    {
        TI = 0;
        SBUF = tx_data[i];
        while (!TI)
            ;
    }
}
unsigned char KeyScan(void) // keyscan
{
    unsigned char tmp = 4;
    unsigned char tmp2 = 0;
    for (unsigned char i = 0; i < 4; i++)
    {
        P0 = (~(1 << i)) | 0xf0;
        unsigned char fts = P0; // four to seven
        unsigned char ztt = P0; // zero to three
        fts = (fts >> 4);
        if ((P0 | 0x0f) != 0xff)
        {
            ztt = (ztt << 4);
            ztt = (ztt >> 4);
        }
        for (unsigned char j = 0; j < 4; j++)
        {
            if (arr[j] == ztt)
            {
                tmp2 = j;
            }
            if (arr[j] == fts)
            {
                tmp = j;
            }
        }
    }
    return seven_segment[tmp * 4 + tmp2];
}
void updateDigits(unsigned char ksr, unsigned char *previousksr, unsigned char *zero_duration)
{
    if (*zero_duration == 0 && ksr != 0b00000000) // debounce
    {
        for (unsigned char i = 3; i > 0; i--)
        {
            Digits[i] = Digits[i - 1];
        }
        Digits[0] = ksr;
        *previousksr = ksr;
    }
    if (ksr == *previousksr)
    {
        (*zero_duration)++;
    }
    else
    {
        *zero_duration = 0;
    }
    if (*zero_duration > 100)
    {
        *zero_duration = 1;
    }
    gx_data[0] = 'G';
    for (unsigned char i = 0; i < 10; i++)
    {
        for (unsigned char k = 0; k < 4; k++)
        {
            if (Digits[k] == seven_segment[i])
            {
                gx_data[4 - k] = i + 0x30;
            }
        }
    }
}

void Timer0_ISR(void) __interrupt(1) __using(1)
{
    TH0 = (65536 - 6250) / 256;
    TL0 = (65536 - 6250) % 256;
    displayDigit(Digits[cnt], cnt);
    cnt++; // interrupt counter + 1
}
void UART_init(void)
{
    TMOD = 0x21; // Timer_1 Mode 2, Timer_0 Mode 1
    T2CON = 0x34;
    // Timer 0 set
    TH0 = (65536 - 6250) / 256; // 表示計數 6250 步後觸發中斷
    TL0 = (65536 - 6250) % 256;
    ET0 = 1; // 啟動 Timer 0 中斷
    TR0 = 1; // 啟動 Timer_0

    // Timer 2 set
    RCAP2H = 0xFF;
    RCAP2L = 0xD9;
    TH2 = RCAP2H;
    TL2 = RCAP2L;
    TR2 = 1; // 啟動 Timer_1

    SCON = 0x50; // SM0=0,SM1=1 Mode 1 , 10 bit. REN=1 Enable receive data
    ES = 1;      // 致能串列埠中斷
    EA = 1;      // 啟動中斷
}

void reset(void)
{
    cnt = 0;
    idx = 0;
    pos = 0;
    // int num, i = 0, j;
    /*while (i < 4)
    {
        num = rand() % 10; // 生成 0 到 9 之間的隨機數字
        for (j = 0; j < i; j++)
        {
            if (random_num[j] == num)
            {
                break; // 如果數字已經存在，跳出內層迴圈
            }
        }
        if (j == i)
        { // 如果數字不重複
            random_num[i] = num;
            i++;
        }
    }*/
    random_num[0] = 1;
    random_num[1] = 2;
    random_num[2] = 3;
    random_num[3] = 4;
}

void uart_isr(void) __interrupt(4) __using(3)
{

    if (RI)
    {
        RI = 0;
        // 接收
        rx_data[idx] = SBUF;
        idx++;
        if (idx == 5)
        {

            // 處理接收到的數據
            switch (rx_data[0])
            {
            case 'G':

                // 判斷猜測結果
                tx_data[0] = 'R';
                tx_data[1] = '0';
                tx_data[2] = 'A';
                tx_data[3] = '0';
                tx_data[4] = 'B';
                for (int i = 0; i < 4; i++)
                {
                    for (int j = 1; j < 5; j++)
                    {
                        if (random_num[i] == rx_data[j] - '0')
                        {
                            if (i == j - 1)
                            {
                                tx_data[1]+=1;
                            }
                            else
                            {
                                tx_data[3]+=1;
                            }
                        }
                    }
                }

                // 組成回復訊息

                txsend(); // tx_data = Rxxxx
                // 答對延遲後傳送重新遊戲
                if (tx_data[1] == 4)
                {
                    reset();
                }
                break;

            case 'R':
                // 收到xAxB的回覆
                Digits[4] = seven_segment[rx_data[1] - '0'];
                Digits[5] = seven_segment[10];
                Digits[6] = seven_segment[rx_data[3] - '0'];
                Digits[7] = seven_segment[11];
                tx_data[0] = 'A';
                txsend(); // 得到回覆後換對方猜

            case 'A':
                // 可以傳送新的數據了
                TI = 0;
                break;

            case 'Z':
                // 接受到重新開始遊戲

                reset();
                break;

            default:
                break;
                // 其他情況的處理
            }
            // reset 接收
            idx = 0;
        }
    }
}

void main(void)
{
    UART_init();
    reset();
    while (1)
    {
        if (cnt >= 8) // 6250*8*1us = 0.05 second
        {
            cnt = 0;
            ksr = KeyScan();
            if (ksr == 0b01110111)
            {
                send();
                
            }

            for (unsigned char i = 0; i < 10; i++)
            {
                if (ksr == seven_segment[i])
                {
                    updateDigits(ksr, &previousksr, &zero_duration);
                }
            }
        }
    }
}
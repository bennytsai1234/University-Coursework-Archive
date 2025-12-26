#include <8051.h>
unsigned char cnt = 0;
char ksr = 0;
unsigned char previousksr = 0;
unsigned char zero_duration = 0;

void displayDigit(unsigned char digit, char position) // display
{
    P2 = digit;
    P1 = 7 - position;
}

static char seven_segment[5][4] = {
    {0b00111111, 0b00000110, 0b01011011, 0b01001111},
    {0b01100110, 0b01101101, 0b01111101, 0b00000111},
    {0b01111111, 0b01101111, 0b01110111, 0b01111100},
    {0b00111001, 0b01011110, 0b01111001, 0b01110001},
    {0b00000000}};
unsigned char Digits[8];
char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};
char KeyScan(void) // keyscan
{
    char tmp = 4;
    char tmp2 = 0;
    for (char i = 0; i < 4; i++)
    {
        P0 = (~(1 << i)) | 0xf0;
        char fts = P0; // four to seven
        char ztt = P0; // zero to three
        fts = (fts >> 4);
        if ((P0 | 0x0f) != 0xff)
        {
            ztt = (ztt << 4);
            ztt = (ztt >> 4);
        }
        for (char j = 0; j < 4; j++)
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
    return seven_segment[tmp][tmp2];
}
void updateDigits(char ksr, unsigned char *previousksr, unsigned char *zero_duration)
{
    if (*zero_duration == 0 && ksr != 0b00000000) // debounce
    {
        for (char i = 7; i > 0; i--)
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
}

void t0_init(void)
{
    TH0 = (65536 - 6250) / 256; // 表示計數 6250 步後觸發中斷
    TL0 = (65536 - 6250) % 256;
    TMOD = (TMOD & 0xF0) | 0x01; // 設定 Timer_0 為 Mode 1
    ET0 = 1;                     // 啟動 Timer 0 中斷
    TR0 = 1;                     // 啟動 Timer_0
    EA = 1;                      // enable interrpt
}

void Timer0_ISR(void) __interrupt(1) __using(1)
{
    TH0 = (65536 - 6250) / 256;
    TL0 = (65536 - 6250) % 256;
    displayDigit(Digits[cnt], cnt);
    cnt++; // interrupt counter + 1
}

void main(void)
{
    t0_init(); // init
    while (1)
    {
        if (cnt >= 8) // 6250*8*1us = 0.05 second
        {
            cnt = 0;
            ksr = KeyScan();
            updateDigits(ksr, &previousksr, &zero_duration);
        }
    }
}
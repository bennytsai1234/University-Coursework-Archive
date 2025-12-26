#include <8051.h>
#define NOTE_DURATION 15625
#define C4 61722
#define D4 62131
#define E4 62502
#define F4 62671
#define G4 62985
#define A4 63263
#define B4 63511
#define C5 63629
#define D5 63835
#define E5 64020
#define F5 64103
#define G5 64260
#define A5 64400
#define B5 64524
#define C6 64582
#define D6 64686
#define E6 64778
#define F6 64820
#define G6 64898
#define A6 64968
#define B6 65030
#define C7 65059
#define D7 65110
#define E7 65157
#define F7 65178
#define G7 65217
#define A7 65252
#define B7 65282
#define SF5 62834
#define RESET 65536

unsigned int index = 0;
unsigned int duration = 0;
unsigned int cnt = 0;
// 音符及其持續時間
const unsigned long note_and_duration[][2] = {

    {REST,4},{REST,4},{E6, 2},{E6, 2},{G6, 2},

    {A6, 2},{G6, 2},{A6, 2},{C7, 2},{B6, 2},{A6, 2},{G6, 4},{A6, 1},{G6, 1},{E6, 6},{REST, 2},{E6, 2},{E6, 2},{G6, 2},{A6, 2},{G6, 2},{A6, 2},{C7, 2},{B6, 2},{A6, 2},{A6, 2},{E6, 4},{D6, 6},{REST, 2},{A6, 2},{D7, 4},
    
    {A6, 2},{D7, 6},{REST, 2},{A6, 2},{D7, 3},{A6, 2},{B6, 4},{E6, 4},{REST, 2},{D6, 2},{E6, 2},{D6, 2},{G6, 4},{REST, 2},{D6, 2},{G6, 2},{A6, 2},{B6, 2},{C7, 2},{B6, 1},{A6, 1},{B6, 6},{REST, 2},{E6, 2},{E6, 2},{G6, 2},

    {A6,2},{G6,2},{A6,2},{C7,2},{B6,2},{A6,2},{G6,2},{A6,4},{E6,6},{REST,2},{E6,2},{E6,2},{G6,2},{A6,2},{G6,2},{C7,2},{B6,2},{A6,2},{A6,2},{G6,4},{E7,6},{REST,2},{A6,2},{D7,3},{A6,1},

    {D7,4},{REST,4},{REST,2},{E7,2},{B6,3},{A6,1},{B6,1},{C7,1},{B6,6},{REST,4},{A6,2},{D7,2},{B6,2},{E6,2},{A6,2},{D7,2},{B6,2},{E6,2},{A6,3},{G6,1},{A6,4},{REST,4},{REST,4},{G7,2},{E7,2},

    {D7,4},{REST,2},{D7,2},{D7,2},{E7,2},{C7,2},{D7,2},{E7,4},{REST,4},{REST,4},{G7,2},{E7,2},{D7,4},{REST,2},{D7,2},{D7,2},{G6,2},{E7,3},{F7,2},{E7,4},{REST,4},{REST,2},{E7,2},{E7,2},

    {B7,6},{E7,1},{D7,1},{D7,4},{C7,2},{B6,2},{C7,2},{D7,2},{E7,2},{A7,6},{A6,2},{C7,2},{E7,2},{D7,2},{A6,2},{C7,2},{B6,4},{G6,4},{A6,4},{REST,4},{REST,4},{G7,2},{E7,2},

    {D7,4},{REST,2},{D7,2},{D7,2},{E7,2},{C7,2},{D7,2},{E7,4},{REST,4},{REST,4},{G7,2},{E7,2},{D7,2},{REST,2},{D7,2},{G6,2},{E7,3},{F7,1},{E7,4},{REST,4},{REST,4},{E7,2},{E7,2},

    {B7,6},{E7,1},{D7,1},{D7,4},{C7,2},{B6,2},{C7,2},{D7,2},{E7,2},{A7,6},{A6,2},{C7,2},{E7,2},{D7,2},{A6,2},{C7,2},{B6,4},{G6,4},{A6,4},{REST,4},{REST,4},{REST,4}
    };
// 定義計時器中斷服務程序
void timer0_isr(void) __interrupt(1) __using(1)
{
    // 重新加載 Timer0 以保持 0.03125 秒的間隔
    TH0 = (65536 - NOTE_DURATION) / 256;
    TL0 = (65536 - NOTE_DURATION) % 256;

    if (cnt == 10) // 31250
    {
        cnt = 0;
        if (index < sizeof(note_and_duration) / sizeof(note_and_duration[0]))
        {
            if (duration == 0)
            {

                duration = note_and_duration[index][1];
                if (note_and_duration[index][0] != REST)
                {
                    // 如果不是休止音符,則更新 Timer1 的頻率
                    TH1 =  note_and_duration[index][0] / 256;
                    TL1 = note_and_duration[index][0] % 256;
                }
                else
                {
                    // 如果是休止音符,則停止 Timer1
                    TH1 = 1;
                    TL1 =1;
                }
                index++;
                if (index >= sizeof(note_and_duration) / sizeof(note_and_duration[0]))
                {
                    index = 0;
                    TH1 = 1;
                    TL1 = 1;
                }
            }
            duration--;
        }
    }
    cnt++;
}

// 定義 Timer1 中斷服務程序
void timer1_isr(void) __interrupt(3) __using(1)
{
    if (index < sizeof(note_and_duration) / sizeof(note_and_duration[0]))
    {
        // 切換蜂鳴器輸出
        TH1 = note_and_duration[index][0] / 256;
        TL1 = note_and_duration[index][0] % 256;
        P3_4 = !P3_4;
    }
}

int main()
{
    // 設置 Timer0 和 Timer1
    TMOD = 0x11;
    TH0 = (65536 - NOTE_DURATION) / 256;
    TL0 = (65536 - NOTE_DURATION) % 256;
    TH1 = 0;
    TL1 = 0;
    P3 = 0b00001000;
    // 啟動 Timer0 和 Timer1
    TR0 = 1;
    TR1 = 1;

    // 啟用中斷
    EA = 1;
    ET0 = 1;
    ET1 = 1;

    while (1)
        ;
}
#include <8051.h>

unsigned char cnt = 0;
char ksr = 0;
unsigned char Digits[8];

static unsigned char seven_segment[18] = {
    0b00111111, 0b00000110, 0b01011011, 0b01001111,
    0b01100110, 0b01101101, 0b01111101, 0b00000111,
    0b01111111, 0b01101111, 0b01110111, 0b01111100,
    0b00111001, 0b01011110, 0b01111001, 0b01110001,
    0b00000000, 0b10000000};

unsigned char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};

void setResolution(unsigned char resolution);

void displayDigit(unsigned char digit, unsigned char position)
{
    P2 = digit;
    P1 = 7 - position;
}

void KeyScan(void)
{
    char tmp = 0b10000000;
    char tmp2 = 0b10000000;
    for (unsigned char i = 0; i < 4; i++)
    {
        P0 = (~(1 << i)) | 0xf0;
        unsigned char fts = P0; // Four to Seven bits
        unsigned char ztt = P0; // Zero to Three bits
        fts = (fts >> 4) & 0x0F;
        ztt = (~P0) & 0x0F;

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
    P0 = 0xf0;
    if (tmp != 0b10000000)
    {
        ksr = tmp;
    }
}

void t0_init(void)
{
    TH0 = (65536 - 5000) / 256;
    TL0 = (65536 - 5000) % 256;
    TMOD = (TMOD & 0xF0) | 0x01;
    ET0 = 1;
    TR0 = 1;
    EA = 1;
    EX0 = 1;
    IT0 = 1;
    P0 = 0xf0;
}

void Timer0_ISR(void) __interrupt(1) __using(1)
{
    TH0 = (65536 - 5000) / 256;
    TL0 = (65536 - 5000) % 256;
    IT0 = 1;
    if (cnt >= 4)
    {
        cnt = 0;
    }
    displayDigit(Digits[cnt], cnt);
    cnt++;
    EX0 = 1;
}

unsigned char resolution[4] = {0, 1, 2, 3};

void External_ISR(void) __interrupt(0) __using(1)
{
    KeyScan();
    setResolution(resolution[ksr]);
    EX0 = 0;
}

unsigned char sensorBuffer[2];

void delay(unsigned int i)
{
    while (i--)
        ;
}

void init_1W(void)
{
    P3_3 = 1;
    delay(8);
    P3_3 = 0;
    delay(80);
    P3_3 = 1;
    delay(14);
    delay(20);
}

unsigned char readByte_1W(void)
{
    unsigned char i = 0;
    unsigned char dat = 0;
    for (i = 8; i > 0; i--)
    {
        P3_3 = 0;
        dat >>= 1;
        P3_3 = 1;
        if (P3_3)
            dat |= 0x80;
        delay(4);
    }
    return dat;
}

void writeByte_1W(unsigned char dat)
{
    unsigned char i = 0;
    for (i = 8; i > 0; i--)
    {
        P3_3 = 0;
        P3_3 = dat & 0x01;
        delay(5);
        P3_3 = 1;
        dat >>= 1;
    }
    delay(4);
}

void read_sensor(void)
{
    init_1W();
    writeByte_1W(0xCC); // Skip ROM
    writeByte_1W(0x44); // Convert T

    init_1W();
    writeByte_1W(0xCC); // Skip ROM
    writeByte_1W(0xBE); // Read Scratchpad

    sensorBuffer[0] = readByte_1W();
    sensorBuffer[1] = readByte_1W();
}

void setResolution(unsigned char resolution)
{
    init_1W();
    writeByte_1W(0xCC); // Skip ROM
    writeByte_1W(0x4E); // Write Scratchpad

    // Write TH, TL and configuration register
    writeByte_1W(0x00);            // TH
    writeByte_1W(0x00);            // TL
    writeByte_1W(resolution << 5); // Configuration register

    init_1W();
    writeByte_1W(0xCC); // Skip ROM
    writeByte_1W(0x48); // Copy Scratchpad to EEPROM
}

void main(void)
{
    t0_init();
    int returntemp;

    while (1)
    {
        EA = 0;
        read_sensor();
        EA = 1;
        returntemp = sensorBuffer[0] | (sensorBuffer[1] << 8);
        float temperature = returntemp * 0.0625;
        int temp = (int)(temperature * 100);

        Digits[0] = seven_segment[temp % 10];
        temp /= 10;
        Digits[1] = seven_segment[temp % 10];
        temp /= 10;
        Digits[2] = seven_segment[temp % 10] | seven_segment[17];
        temp /= 10;
        Digits[3] = seven_segment[temp % 10];
    }
}
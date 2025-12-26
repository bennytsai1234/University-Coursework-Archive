#include <8051.h>
#include "Keypad4x4.h"

static char seven_segment[5][4] = {
    {0b00111111, 0b00000110, 0b01011011, 0b01001111},
    {0b01100110, 0b01101101, 0b01111101, 0b00000111},
    {0b01111111, 0b01101111, 0b01110111, 0b01111100},
    {0b00111001, 0b01011110, 0b01111001, 0b01110001},
    {0b00000000}};
unsigned char Digits[8];
char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};
char KeyScan()
{
    char tmp = 4;
    char tmp2 = 0;
    for (char i = 0; i < 4; i++)
    {
        P0 = (~(1 << i)) | 0xf0;
        char fts = P0;
        char ztt = P0;
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
    if (*zero_duration == 0 && ksr != 0b00000000)
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

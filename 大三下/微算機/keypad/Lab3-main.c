#include "LED_Display.h"
#include "Keypad4x4.h"

extern unsigned char Digits[8];

void main()
{
    char ksr = 0;
    unsigned char previousksr = 0;
    unsigned char zero_duration = 0;
    while (1)
    {
        ksr = KeyScan();
        updateDigits(ksr, &previousksr, &zero_duration);

        for (char i = 0; i < 8; i++)
        {
            displayDigit(Digits[i], i);
        }
    }
}

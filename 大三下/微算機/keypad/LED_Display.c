#include <8051.h>
#include "LED_Display.h"

void displayDigit(unsigned char digit, char position)
{
    P2 = digit;
    switch (position)
    {
    case 3:
        P1 = 0b00000011;
        break;
    case 2:
        P1 = 0b00000010;
        break;
    case 1:
        P1 = 0b00000001;
        break;
    case 0:
        P1 = 0b00000000;
        break;
    case 7:
        P1 = 0b00000111;
        break;
    case 6:
        P1 = 0b00000110;
        break;
    case 5:
        P1 = 0b00000101;
        break;
    case 4:
        P1 = 0b00000100;
        break;
    }
    for (unsigned char j = 0; j < 255; j++)
    {
    }
}

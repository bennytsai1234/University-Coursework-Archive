#include <8051.h>

void main()
{
    // LED 的模式
    unsigned char patterns[] = {
        0b11100111,
        0b11011011,
        0b10111101,
        0b01111110,
        0b10111101,
        0b11011011};

    while (1)
    {
        for (unsigned char i = 0; i < 6; i++)
        {
            P2 = patterns[i];
            short count =10000;
            while (count--);
        }
    }
}

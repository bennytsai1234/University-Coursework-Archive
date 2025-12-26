#ifndef __KEYPAD4X4_H__
#define __KEYPAD4X4_H__

char KeyScan();
void updateDigits(char ksr, unsigned char *previousksr, unsigned char *zero_duration);

#endif // __KEYPAD4X4_H__

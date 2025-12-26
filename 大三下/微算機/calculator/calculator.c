#include <8051.h>

// 定義一些全域變數
unsigned char cnt = 0;            // 中斷計數器
unsigned char ksr = 0;            // 當前鍵掃描結果
unsigned char previousksr = 0;    // 前一次的鍵掃描結果
unsigned char zero_duration = 0;  // 持續按鍵的時間
int a = 0;                        // 操作數 a
int b = 0;                        // 操作數 b
unsigned char c = 0;              // 運算類型
int d = 0;                        // 計算結果
unsigned char e = 0;              // 運算標誌

// 顯示數字到七段顯示器的函數
void displayDigit(unsigned char digit, char position) {
    P2 = digit;                // 設置數字
    P1 = 7 - position;         // 設置位置
}

// 定義七段顯示器的段碼
static unsigned char seven_segment[17] = {
    0b00111111, 0b00000110, 0b01011011, 0b01001111,
    0b01100110, 0b01101101, 0b01111101, 0b00000111,
    0b01111111, 0b01101111, 0b01110111, 0b01111100,
    0b00111001, 0b01011110, 0b01111001, 0b01110001,
    0b00000000
};

unsigned char Digits[8];       // 存儲顯示的數字
unsigned char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};

// 鍵掃描函數
unsigned char KeyScan(void) {
    unsigned char tmp = 4;
    unsigned char tmp2 = 0;
    for (unsigned char i = 0; i < 4; i++) {
        P0 = (~(1 << i)) | 0xf0;
        unsigned char fts = P0; // 四到七位的掃描結果
        unsigned char ztt = P0; // 零到三位的掃描結果
        fts = (fts >> 4);
        if ((P0 | 0x0f) != 0xff) {
            ztt = (ztt << 4);
            ztt = (ztt >> 4);
        }
        for (unsigned char j = 0; j < 4; j++) {
            if (arr[j] == ztt) {
                tmp2 = j;
            }
            if (arr[j] == fts) {
                tmp = j;
            }
        }
    }
    return seven_segment[tmp * 4 + tmp2];
}

// 更新顯示的數字
void updateDigits(unsigned char ksr, unsigned char *previousksr, unsigned char *zero_duration) {
    if (*zero_duration == 0 && ksr != 0b00000000) { // 消除抖動
        for (unsigned char i = 7; i > 0; i--) {
            Digits[i] = Digits[i - 1];
        }
        Digits[0] = ksr;
        *previousksr = ksr;
        for (int i = 0; i < 10; i++) {
            if (ksr == seven_segment[i]) {
                a *= 10;
                a += i;
            }
        }
        // 根據按鍵判斷操作類型
        if (ksr == seven_segment[10]) {
            c = 1; // 加法
            d = a;
            a = 0;
        }
        if (ksr == seven_segment[11]) {
            c = 2; // 減法
            d = a;
            a = 0;
        }
        if (ksr == seven_segment[12]) {
            c = 3; // 乘法
            d = a;
            a = 0;
        }
        if (ksr == seven_segment[13]) {
            c = 4; // 除法
            d = a;
            a = 0;
        }
        if (ksr == seven_segment[14]) {
            e = 1; // 運算標誌
        }
        if (ksr == seven_segment[15]) {
            // 清除所有數據
            a = 0;
            b = 0;
            c = 0;
            d = 0;
            e = 0;
            for (int i = 0; i < 8; i++) {
                Digits[i] = seven_segment[16];
            }
        }
    }
    if (ksr == *previousksr) {
        (*zero_duration)++;
    } else {
        *zero_duration = 0;
    }
    if (*zero_duration > 100) {
        *zero_duration = 1;
    }
}

// 初始化定時器0
void t0_init(void) {
    TH0 = (65536 - 6250) / 256; // 設置高8位
    TL0 = (65536 - 6250) % 256; // 設置低8位
    TMOD = (TMOD & 0xF0) | 0x01; // 設置定時器0為模式1
    ET0 = 1;                     // 啟動定時器0中斷
    TR0 = 1;                     // 啟動定時器0
    EA = 1;                      // 啟用所有中斷
}

// 定時器0中斷服務程序
void Timer0_ISR(void) __interrupt(1) __using(1) {
    TH0 = (65536 - 6250) / 256;
    TL0 = (65536 - 6250) % 256;
    displayDigit(Digits[cnt], cnt); // 顯示數字
    cnt++; // 中斷計數器加1
}

// 主函數
void main(void) {
    t0_init(); // 初始化定時器

    while (1) {
        if (cnt >= 8) { // 6250*8*1us = 0.05秒
            cnt = 0;
            ksr = KeyScan(); // 鍵掃描
            if (e == 1) {
                // 根據運算類型進行計算
                switch (c) {
                case 1:
                    d += a;
                    break;
                case 2:
                    if (a > d) {
                        d = a - d;
                    } else {
                        d = d - a;
                    }
                    break;
                case 3:
                    d *= a;
                    break;
                case 4:
                    d /= a;
                    break;
                default:
                    break;
                }
                b = d;
                for (int i = 0; i < 8; i++) {
                    if (d != 0) {
                        Digits[i] = seven_segment[d % 10];
                    } else {
                        Digits[i] = seven_segment[16];
                    }
                    d /= 10;
                }
                a = b;
                c = 0;
                e = 0;
            }
            updateDigits(ksr, &previousksr, &zero_duration); // 更新顯示數字
        }
    }
}

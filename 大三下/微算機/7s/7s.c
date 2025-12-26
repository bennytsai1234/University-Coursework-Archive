#include <8051.h>  

// 七段顯示器的數字碼表
const char seven_segment[10] = {
    0b00111111, // 0
    0b00000110, // 1
    0b01011011, // 2
    0b01001111, // 3
    0b01100110, // 4
    0b01101101, // 5
    0b01111101, // 6
    0b00000111, // 7
    0b01111111, // 8
    0b01101111  // 9
};

unsigned char Digits[4];  // 存放四位數字的數組

// 設置顯示的數字
void setNumber(unsigned int number)
{
    if (number >= 1000)
        Digits[0] = seven_segment[number / 1000 % 10];
    else
        Digits[0] = 0b00000000; // 千位數字
    if (number >= 100)
        Digits[1] = seven_segment[number / 100 % 10];
    else
        Digits[1] = 0b00000000; // 百位數字
    if (number >= 10)
        Digits[2] = seven_segment[number / 10 % 10];
    else
        Digits[2] = 0b00000000;             // 十位數字
    Digits[3] = seven_segment[number % 10]; // 個位數字
}

void main()
{
    P3 = 0b00000100;  // 初始化 P3 為二進位 00000100
    unsigned int num = 0;  // 初始化數字 num 為 0
    unsigned char previousP3 = P3;  // 存儲上一次的 P3 值
    unsigned char i;
    unsigned char zero_duration = 0;  // P3 為 0 的持續時間
    unsigned char isReset = 0;  // 是否需要重置計數器

    while (1)
    {
        // 如果 P3 從 0 變為非零
        if (previousP3 == 0b00000000 && P3 == 0b00000100 && !isReset)
        {
            num++;  // 數字加一
        }
        // 如果 P3 從 0 變為非零且需要重置
        else if (previousP3 == 0b00000000 && P3 == 0b00000100 && isReset)
        {
            isReset = 0;  // 重置為 0
        }
        previousP3 = P3; // 存儲當前的 P3 值，供下一次迭代使用
        setNumber(num);  // 設置顯示的數字

        // 如果 P3 為 0，持續時間加一
        if (P3 == 0b00000000)
        {
            zero_duration++;
        }
        else
        {
            zero_duration = 0; // 如果 P3 不為 0，重置計數器
        }

        // 如果 P3 持續為 0 超過一定時間
        if (zero_duration > 100)
        {
            setNumber(0);  // 設置顯示的數字為 0
            num = 0;           // 重置 num
            zero_duration = 0; // 重置計數器
            isReset = 1;   // 設置為重置狀態
        }
        
        // 顯示四位數字
        for (i = 0; i < 4; i++)
        {
            P2 = Digits[i];  // 在 P2 顯示該位的數字碼
            switch (i)
            {
            case 0:
                P1 = 0b00000100;  // 控制第一位的顯示
                break;
            case 1:
                P1 = 0b00000101;  // 控制第二位的顯示
                break;
            case 2:
                P1 = 0b00000110;  // 控制第三位的顯示
                break;
            case 3:
                P1 = 0b00000111;  // 控制第四位的顯示
                break;
            }

            for (unsigned j = 0; j < 255; j++)  // 簡單的延時
            {
            }
        }
    }
}

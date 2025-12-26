#include <8051.h>

// Assembly subroutine prototypes
extern void non_reentrant_display(unsigned char, unsigned char);         // 宣告非可重入顯示函數的原型
extern void reentrant_display(unsigned char, unsigned char) __reentrant; // 宣告可重入顯示函數的原型

void main()
{
    while (1) // 進入無限循環
    {
        for (unsigned char i = 0; i < 8; ++i) // 迭代0到7的數字
        {
            if (i % 2 == 0) // 判斷奇偶性
            {
                non_reentrant_display(i, i); // 使用非可重入顯示函數顯示偶數位
            }
            else
            {
                reentrant_display(i, i); // 使用可重入顯示函數顯示奇數位
            }
            for (unsigned char j = 0; j < 255; j++) // 產生延遲
            {
            }
        }
    }
}

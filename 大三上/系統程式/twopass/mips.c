#include <stdio.h>

int main() {
    int a = 5; // 這裡設置a和b的值，你可以根據需要更改它們
    int b = 4;
    int D[20]; // 假設D陣列的大小足夠存放計算結果

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            D[4 * j] = i + j;
        }
    }

    // 顯示計算結果
    for (int k = 0; k < a * b; k++) {
        printf("D[%d] = %d\n", k, D[k]);
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;


int main() {
    // 使用 std::numeric_limits<int>::max() 獲取 int 的最大值
    std::cout << "最大的 int 值: " << std::numeric_limits<int>::max() << std::endl;

    // 使用 RAND_MAX 獲取 rand() 函數的最大值
    std::cout << "rand() 函數的最大值: " << RAND_MAX << std::endl;

    return 0;
}

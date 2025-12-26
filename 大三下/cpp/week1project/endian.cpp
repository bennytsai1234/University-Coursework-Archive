#include <iostream>
using namespace std;

int main() {
    const unsigned int n = 163u * 256 * 256 * 256 + 17 * 256 * 256 + 22 * 256 + 162;
    const unsigned char* c = reinterpret_cast<const unsigned char*>(&n);
    cout << static_cast<int>(*c) << '.'  // 打印第一個位元組
         << static_cast<int>(*(c + 1)) << '.'  // 打印第二個位元組
         << static_cast<int>(*(c + 2)) << '.'  // 打印第三個位元組
         << static_cast<int>(*(c + 3)) << '.'; // 打印第四個位元組
    return 0;
}

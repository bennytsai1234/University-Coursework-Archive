// Pointer to Function
#include <iostream>

int add     (int a, int b) { return a+b; }
int subtract(int a, int b) { return a-b; }
int multiply(int a, int b) { return a*b; }
int divide  (int a, int b) { return a/b; }

int main() {
    int *f[](int, int) = {add, subtract, multiply, divide};
    for (int i=0; i<4; ++i)
        std::cout << f[i](7, 3) << ' ';
    return 0;
}
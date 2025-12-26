#include <iostream>
using namespace std;

class CRational
{
public:
    int p;
    int q;
    CRational()
    { // 添加預設建構子
        p = 0;
        q = 1;
    }
    CRational(int a, int b)
    {
        p = a;
        q = b;
    }
};

int main()
{
    CRational a(1,2);
    a.p = 3;
    a.q = 2; // 創建一個有理數對象，分子為3，分母為4
    cout << "分子: " << a.p << ", 分母: " << a.q << endl;
    return 0;
}

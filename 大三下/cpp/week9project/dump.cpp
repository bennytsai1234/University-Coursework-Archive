#include <iostream>
#include <iomanip>
using std::cout;
using std::endl;
using std::setprecision;
using std::setw;
int main()
{
    float b[] = {3.14159, .5, 100.75};
    for (int i = 0; i < 3; ++i)
        cout << setw(3) << b[i] << endl;
    for (int i = 0; i < 3; ++i)
        cout << setprecision(3) << b[i] << endl;
    for (int i = 0; i < 3; ++i)
        cout << std::fixed << setprecision(3) << b[i] << endl;
    for (int i = 0; i < 3; ++i)
        cout <<setw(7) << std::fixed << setprecision(3) << b[i] << endl;
    return 0;
}
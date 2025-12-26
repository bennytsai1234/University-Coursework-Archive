#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::istream;
using std::ostream;

#include "rational.h"

int main()
{
    CRational a, b, c;
    cin >> a >> b;
    c = a + b;
    cout << c << endl;
    return 0;
}
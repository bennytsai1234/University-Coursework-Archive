#include <iostream>
#include "rational.h"
using std::cout;
using std::endl;

int main() {
    CRational a(2, 8);
    CRational b("3/4");
    CRational d("2");
    cout << a << endl;
    cout << a + b << endl;
    cout << d - a << endl;
    return 0;
} 
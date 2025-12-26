#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::endl;
#include "request.h"

#define WWW     "http://lilina.csie.ncnu.edu.tw:8000/"
int main() {
    CRequest request;
    string html;

    html = request.urlopen(WWW).read();
    cout << html << endl;

    html = request.urlopen(WWW "ex01", "A=5&B=3").read();
    cout << html << endl;
    return 0;
}

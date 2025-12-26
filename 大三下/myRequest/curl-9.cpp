#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::endl;
#include "myrequest.h"

#define URL     "http://lilina.csie.ncnu.edu.tw:8000/"
int main() {
    MyRequest http(URL);
    string html;

    http >> html;
    cout << html << endl;
     
    http.setUrl("http://lilina.csie.ncnu.edu.tw:8000/ex01");
    http << "A=3&B=4" >> html;
    cout << html << endl;
    return 0;
}

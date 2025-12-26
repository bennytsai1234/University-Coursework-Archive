#include "rational.h"
#include <iostream>
using std::cin;
using std::cout; 
using std::getline;
using std::endl;

int main()
{
    string line;
    while (getline(cin, line))
    {
        int plus_position = line.find("+");
        if (plus_position != std::string::npos)
        {
            CRational first(line.substr(0, plus_position));
            CRational second(line.substr(plus_position + 1));
            cout << (first + second) << endl;
        }
    }
}

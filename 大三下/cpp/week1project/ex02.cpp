#include <iostream>
#include <ctime>
using namespace std;

int main() {
    time_t t;
    struct tm *now;
    time(&t);
    now = localtime(&t);
    cout << now->tm_year+1900 << "-" << now->tm_mon +1<< "-" << now->tm_mday << endl;
    return 0;
}

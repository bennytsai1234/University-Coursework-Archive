#include<bits/stdc++.h>

using namespace std;

int main()
{
    char a[10];
    for (size_t i = 0; i < 10; i++)
    {
        /* code */
        a[i]= i+'0';
    }
    
    char *i = a;
    cout<<*i<<*(i+1);

    return 0;
}
#include <bits/stdc++.h>
using namespace std;
int shift(int a ,int b)
{
    while (a!=b){
        a=a/2;
        b=b*2;
    }
    return a;
}
void main (){
    int a=4096;
    int b=1;
    int ans=0;
    ans=shift(a,b);
}
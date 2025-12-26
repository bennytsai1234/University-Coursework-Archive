#include <bits/stdc++.h>
using namespace std;
void main()
{
    int ans = 0;
    int cnt = 6;
    for (int i = 0; i < cnt; i++)
    {
        switch (i % 3)
        {
        case 0:
            ans += 1;
            break;
        case 1:
            ans += 3;
            break;
        case 2:
            ans -= 1;
            break;
        }
    }
}
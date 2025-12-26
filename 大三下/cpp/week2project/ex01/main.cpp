#include <iostream>
#include "listElement.h"
using std::cin;

ListElement* addFront(ListElement* pList, int v);
void printList(ListElement* p);

int main()
{
    ListElement* pList = NULL;
    int n;
    while (true)
    {
        cin >> n;
        if (n <= 0) break;
        pList = addFront(pList, n);
    }
    printList(pList);
    return 0;
}
#include <iostream>
#include "listElement.h"
using std::cin;

ListElement* insertToList(ListElement* pList, int v);
void printList(ListElement* p);

int main()
{
    ListElement* pList = NULL;
    int n;
    while (cin >> n)
    {
        if (n <= 0) break;
        pList = insertToList(pList, n);
    }
    printList(pList);
    return 0;
}
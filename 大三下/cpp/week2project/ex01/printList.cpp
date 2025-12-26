#include <iostream>
#include "listElement.h"

void printList(ListElement* p)
{
    while (p != NULL)
    {
        std::cout << p->value << ' ';
        p = p->pNext;
    }
    std::cout << std::endl;
}
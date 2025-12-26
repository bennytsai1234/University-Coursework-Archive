#include "listElement.h"
#include <iostream>

ListElement *insertToList(ListElement *pList, int newValue)
{
    ListElement *newNode = new ListElement;
    newNode->value = newValue;

    if (pList == NULL || newValue < pList->value)
    {
        newNode->pNext = pList;
        return newNode;
    }

    ListElement *current = pList;
    while (current->pNext != NULL && current->pNext->value < newValue)
    {
        current = current->pNext;
    }

    newNode->pNext = current->pNext;
    current->pNext = newNode;

    return pList;
}

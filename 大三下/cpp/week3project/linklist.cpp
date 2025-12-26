#include<iostream>
using namespace std;

struct Node
{
    int value;
    Node* next;
    /* data */
};

Node* insertToList(Node* head, int v){
    Node* p = new Node;
    p -> value = v;
    p -> next = head;
    return p;
}

void printList(Node* p){
    if(p){
        cout << p -> value;
        printList(p -> next);
    }
}

int main(){
    int a[] = {26, 59, 41, 31};
    Node* pList = nullptr;
    for(size_t i = 0; i < sizeof(a)/sizeof(a[0]); ++i)
        pList = insertToList(pList, a[i]);
    printList(pList);
    return 0;
}
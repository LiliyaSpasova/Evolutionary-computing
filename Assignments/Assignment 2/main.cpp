#include <iostream>
#include "DoublyLinkedList.h"
using namespace std;
int main()
{
    DoublyLinkedList *dll = new DoublyLinkedList(5);
    dll->insert(20);
    dll->insert(10);
    dll->insert(-6);
    dll->insert(2);
    dll->insert(4);
    dll->print();
    dll->deleteVal(20);
    dll->print();
    dll->deleteVal(4);
    dll->print();
    dll->deleteVal(18);
    dll->print();
}
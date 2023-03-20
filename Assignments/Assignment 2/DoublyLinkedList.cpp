#include <iostream>
using namespace std;
#include "DoublyLinkedList.h"

void DoublyLinkedList::print()
{
    while (head != NULL)
    {
        cout << head->data << " -> ";
        head = head->next;
    }
}
void DoublyLinkedList::insert(int value)
{
    Node *node = new Node(value);
    if (head != nullptr)
    {
        head->prev = node;
    }
    head = node;
}
Node* DoublyLinkedList::searchNode(int val){
        Node* curr=head;
        while(curr!=nullptr){
            if(curr->data==val){
               
                return curr;
            }
            curr=curr->next;
        }
        return nullptr;
    }
void DoublyLinkedList::deleteVal(int value)
{
    Node *temp = searchNode( value );
    if ( temp != nullptr )
    {
        if ( temp->next != nullptr )
        {
            temp->next->prev = temp->prev;
        }

        if ( temp->prev != nullptr )
        {
            temp->prev->next = temp->next;
        }
        else
        {
            head = temp->next;
        }
        delete temp;
    }
}
#include <iostream>
using namespace std;
#include "DoublyLinkedList.h"

void DoublyLinkedList::print()
{
    Node* curr=head;
    while (curr != NULL)
    {
        cout << curr->data << " -> ";
        curr = curr->next;
    }
    cout<<"Null";
    cout<<endl;
}
void DoublyLinkedList::insert(int value)
{
    Node *node = new Node(value);
 
    node->next = (this->head);
    node->prev = NULL;
    if ((this->head) !=nullptr)
        (this->head)->prev = node;
 
    /* 5. move the head to point to the new node */
    (this->head) = node;
}
Node* DoublyLinkedList::searchNode(int val)
{
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
    Node *temp = this->searchNode( value );
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
struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(int val)
    {
      this->data=val;
      this->next=nullptr;
      this->prev=nullptr;
    }
};

class DoublyLinkedList {
  public:
    Node* head;
    DoublyLinkedList(){
      head = nullptr;
    }
    DoublyLinkedList(int val){
      head = new Node(val);
    }
    void print();
    void insert(int new_data);
    void deleteVal(int value);
    Node* searchNode (int value);
};
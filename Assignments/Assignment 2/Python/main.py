from List import Node
from List import DoubleLinkedList

def main():
    dllist=DoubleLinkedList()

    #for i in range(5):
       # dllist.append(i)

    dllist.append(0)
    dllist.append(2)
    #dllist.printList()
    
    dllist.insertAfter(2,11)
    dllist.insertBefore(11,'x')
    dllist.insertAfter(11,'x')

    dllist.printList()
    if (dllist.head):
        print("head is ",dllist.head.data)
    
    if(dllist.end):
        print("end is ",dllist.end.data)

main()
    
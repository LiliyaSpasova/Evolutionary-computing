class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.end=None

    def append(self,data):
        if self.head is None:
            newNode =  Node(data)
            newNode.next=None
            newNode.prev=None
            self.head = newNode
            self.end=newNode
        else:
            newNode=Node(data)
            endNode=self.end
            endNode.next=newNode
            newNode.prev=endNode
            newNode.next=None
            self.end=newNode

    def prepend(self,data):
        if self.head is None:
            newNode=Node(data)
            newNode.next=None
            newNode.prev=None
            self.head=newNode
        else:
            newNode=Node(data)
            headNode=self.head
            headNode.prev=newNode
            newNode.next=headNode
            newNode.prev=None
            self.head=newNode

    def insertAfter(self,key,data):
        currentNode = self.head
        while currentNode:
            if ((currentNode.next is None) and (currentNode.data==key)):
                self.append(data)
                return
            elif currentNode.data==key:
                newNode=Node(data)
                nextNode=currentNode.next
                currentNode.next=newNode
                newNode.next=nextNode
                newNode.prev=currentNode
                nextNode.prev=newNode
            currentNode=currentNode.next
        return


    def insertBefore(self,key,data):
        currentNode = self.head
        while currentNode:
            if ((currentNode.prev is None) and (currentNode.data==key)):
                self.prepend(data)
                return
            elif currentNode.data==key:
                newNode=Node(data)
                previousNode=currentNode.prev
                previousNode.next=newNode
                currentNode.prev=newNode
                newNode.next=currentNode
                newNode.prev=previousNode
            currentNode=currentNode.next
        return

    def findNode(self,data):
        result = None
        currentNode=self.head
        while currentNode:
            if (currentNode.data==data):
                result=currentNode
            currentNode=currentNode.next
        return result

    def deleteNode(self,data):
        currentNode=self.head
        while currentNode:
            if (currentNode.data==data):
                #node is head and there are no other nodes
                if ((currentNode.next is None) and (currentNode==self.head)):
                    currentNode=None
                    self.head=None
                    return

                #node is head but there is at least one other node after it
                if ((currentNode.next) and (currentNode==self.head)):
                    newHead=currentNode.next
                    newHead.prev=None
                    self.head=newHead
                    currentNode=None
                    return

                #node is last node
                if ((currentNode.next is None) and (currentNode.prev is not None)):
                    newEnd=currentNode.prev
                    newEnd.next=None
                    currentNode.prev=None
                    currentNode=None
                    self.end=newEnd
                    return

                #node is somewhere in the middle meaning that next and prev are not None
                if ((currentNode.next is not None) and (currentNode.prev is not None)):
                    previousNode=currentNode.prev
                    nextNode=currentNode.next

                    previousNode.next=nextNode
                    nextNode.prev=previousNode

                    currentNode.next=None
                    currentNode.prev=None
                    currentNode=None
                    return
            currentNode=currentNode.next
        return


    def printList(self):
        currentNode=self.head
        while currentNode:
            print(currentNode.data)
            currentNode=currentNode.next


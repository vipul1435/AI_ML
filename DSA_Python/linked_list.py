# This file contains the implementation of linked list in python.

# Node class is used to create a node of linked list.
class Node:
    def __init__(self,data=None,next=None):
        self.data = data # data of node
        self.next = next # next pointer of node

# LinkedList class is used to create a linked list.
class LinkedList:
    def __init__(self):
        self.head = None
    
    # insertAtBegining method is used to insert a node at the begining of linked list.
    def insertAtBegining(self,data):
        temp = Node(data,self.head) # create a new node with data and next pointer as head.
        self.head=temp
    
    # insertAtEnd method is used to insert a node at the end of linked list.
    def insertAtEnd(self,data):
        temp = self.head # temp is used to traverse the linked list.
        while temp and temp.next:  # traverse the linked list till the end.
            temp=temp.next 
        temp.next = Node(data) # create a new node with data and next pointer as None and assign it to the next pointer of last node.

    # print method is used to print the linked list.
    def print(self):
        if self.head is None:
            print("Linked List is emty.")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="-->")
                temp=temp.next
    
    # length method is used to find the length of linked list.
    def length(self):
        counter = 0
        temp = self.head
        while temp:
            counter+=1
            temp=temp.next
        return counter
    
    # removeAt method is used to remove a node from linked list at a given index.
    def removeAt(self,index):
        length = self.length()
        if index<0 or index>=length:
            print("Invalid Index")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        while index>1:
            temp=temp.next
            index-=1
        temp.next = temp.next.next

    # insertAt method is used to insert a node at a given index in linked list.
    def insertAt(self,index,data):
        length = self.length()
        if index<0 or index>length:
            print("invalid index")
            return

        if index == 0:
            self.insertAtBegining(data)
            return

        if index == length:
            self.insertAtEnd(data)
            return

        temp = self.head
        while index>1:
            index-=1
            temp=temp.next
        
        temp.next = Node(data,temp.next)
        return

linkList = LinkedList()
linkList.insertAtBegining(2)
linkList.insertAtBegining(3)
# linkList.insertAtBegining(1)
# linkList.insertAtEnd(5)
# linkList.insertAtBegining(0)
# linkList.insertAtEnd(8)
linkList.print()
# print(f"\n{linkList.length()}")
# linkList.removeAt(5)
# linkList.removeAt(1)
# linkList.print()
print(f"\n{linkList.length()}")
linkList.insertAt(1,99)
linkList.print()

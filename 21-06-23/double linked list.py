class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
        
    def insert_end(self):
        n=Node(300)
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                if temp.next is None:
                    print(temp.data)
                    temp = temp.next
                else:
                    print(temp.data, "<->", end=" ")
                    temp = temp.next



dll = DoubleLinkedList()
n = Node(10)
dll.head = n
n1 = Node(20)
dll.head.next = n1
n1.prev = dll.head
n2 = Node(30)
n1.next = n2
n2.prev = n1
n3 = Node(40)
n2.next = n3
n3.prev = n2
n4 = Node(50)
n3.next = n4
n4.prev = n3
dll.display()

dll.insert_start()
dll.display()
print()
dll.insert_end()
dll.display()
print()
dll.insert_pos(2)
dll.display()
print()

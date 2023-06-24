class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete_beginning(self):
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
        else:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
        else:
            if position == 0:
                self.delete_beginning()
            else:
                temp = self.head
                count = 0
                while temp is not None and count < position:
                    temp = temp.next
                    count += 1
                if temp is None:
                    print("Invalid position. Unable to delete.")
                else:
                    temp.prev.next = temp.next
                    if temp.next is not None:
                        temp.next.prev = temp.prev

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                if temp.next is None:
                    print(temp.data)
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
n5 = Node(60)
n4.next = n5
n5.prev = n4

dll.display()  
dll.insert_beginning(100)
dll.display()  
dll.insert_end(200)
dll.display()  

dll.delete_beginning()
dll.display()  

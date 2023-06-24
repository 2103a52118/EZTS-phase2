class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

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
                    print(temp.data, "->", end=" ")
                    temp = temp.next

    def search_node(self, target):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head
        while temp is not None:
            if temp.data == target:
                print("Node found")
                return
            temp = temp.next

        print("Node not found")


obj = SingleLinkedList()
n = Node(10)
obj.head = n
n1 = Node(20)
obj.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
n5 = Node(60)
n4.next = n5
obj.display()
obj.insert_beginning(100)
obj.display()
obj.search_node(20)
obj.search_node(99)

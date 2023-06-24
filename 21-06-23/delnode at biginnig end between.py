class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_position(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(pos - 2):
                if temp is None:
                    print("Invalid position")
                    return
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None

    def delete_position(self, pos):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        if pos == 1:
            self.head = temp.next
            temp.next = None
            return
        for _ in range(pos - 2):
            if temp is None or temp.next is None:
                print("Invalid position")
                return
            temp = temp.next
        next_node = temp.next.next
        temp.next.next = None
        temp.next = next_node

    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        if prev is None:
            self.head = None
        else:
            prev.next = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "->", end=" ")
                temp = temp.next


obj = SingleLinkedList()
n = Node(10)
obj.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4

obj.display()
print()
obj.insert_position(3, 1000)
obj.display()
print()
obj.delete_position(3)
obj.display()
print()
obj.delete_last()
obj.display()
print()
obj.delete_beginning()
obj.display()

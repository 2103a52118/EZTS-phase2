class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
        curr_node.next = None

    def delete_at_position(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        prev_node = None
        count = 0
        while curr_node and count < position:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if not curr_node:
            return
        prev_node.next = curr_node.next

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

# Create a linked list
linked_list = LinkedList()

# Insert nodes at the end
n = int(input("Enter the number of nodes: "))
print("Enter the node values:")
for _ in range(n):
    value = int(input())
    linked_list.insert_at_end(value)

print("Linked List:")
linked_list.display()

# Delete node at the beginning
linked_list.delete_at_beginning()
print("Linked List after deleting node at the beginning:")
linked_list.display()

# Delete node at the end
linked_list.delete_at_end()
print("Linked List after deleting node at the end:")
linked_list.display()

# Delete node at a specific position (index)
position = int(input("Enter the position to delete (0-based indexing): "))
linked_list.delete_at_position(position)
print(f"Linked List after deleting node at position {position}:")
linked_list.display()

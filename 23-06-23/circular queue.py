class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        elif self.head == self.tail:
            removed_element = self.head.data
            self.head = None
            self.tail = None
            print("Removed element:", removed_element)
        else:
            removed_element = self.head.data
            self.head = self.head.next
            self.tail.next = self.head
            print("Removed element:", removed_element)

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()

    def peek(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print("Front element:", self.head.data)


queue = CircularQueue()

while True:
    print("Select operation: 1. Enqueue 2. Dequeue 3. Display 4. Peek 5. Quit")
    choice = int(input())

    if choice == 1:
        element = int(input("Enter the element: "))
        queue.enqueue(element)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        queue.peek()
    elif choice == 5:
        break
    else:
        print("Enter the correct operation.")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return popped

obj_queue = Queue()

while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do: ').split()
    operation = do[0].strip().lower()

    if operation == 'enqueue':
        if len(do) < 2:
            print('Please provide a value to enqueue.')
            continue
        obj_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = obj_queue.dequeue()
        if dequeued is None:
            print('Queue is empty')
        else:
            print('Dequeued value:', dequeued)
    elif operation == 'quit':
        break
    else:
        print('Invalid operation. Please try again.')

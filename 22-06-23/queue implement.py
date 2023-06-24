queue = []

def enqueue():
    element = int(input("Enter the element: "))
    queue.append(element)
    print(queue)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("Removed element:", e)
        print(queue)

def display():
    if not queue:
        print("Queue is empty")
    else:
        print(queue)

def peek():
    if not queue:
        print("Queue is empty")
    else:
        print(queue[0])

while True:
    print("Select operation: 1. Enqueue 2. Dequeue 3. Display 4. Peek 5. Quit")
    choice = int(input())

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        peek()
    elif choice == 5:
        break
    else:
        print("Enter the correct operation.")

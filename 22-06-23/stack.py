stack=[]
def push():
    element=int(input("enter the elements"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
def peak():
    print(stack[0])
    
while True:
    print("select operations 1.push 2.pop 3. display 4.peak 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        peak()
    elif choice==5:
        break 
    else:
        print("enter the correct operations")
        

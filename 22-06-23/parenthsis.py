def is_balanced(parentheses):
    stack = []
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    
    for p in parentheses:
        if p in opening:
            stack.append(p)
        elif p in closing:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if opening.index(top) != closing.index(p):
                return False
    
    return len(stack) == 0

input_parentheses = input("Enter a combination of parentheses: ")

if is_balanced(input_parentheses):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")

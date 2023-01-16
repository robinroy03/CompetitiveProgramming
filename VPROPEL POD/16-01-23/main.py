q  = int(input())

stack = []

def puzzle(color):
    if len(stack) >=3:
        if stack[-1] == stack[-2] == stack[-3] == color:
            return True
    return False

for _ in range(q):
    i = input()
    if i == '2':
        print(len(stack))
    else:
        k, color = i.split()
        
        if len(stack) != 0:
            if stack[-1] == color:
                if puzzle(color):
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.pop(-1)
        
                    continue
        
        stack.append(color)

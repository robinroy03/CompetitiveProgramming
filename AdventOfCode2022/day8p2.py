with open("day8.txt",'r') as f:
    l=f.readlines()

row_count=len(l)
column_count=len(l[0])-1

def left(x,xi,i):
    row=l[i]
    counter=0
    for r in range(xi-1,-1,-1):
        counter+=1
        if int(row[r])>=x:
            break
    return counter

def right(x,xi,i):
    row=l[i]
    counter=0
    for r in range(xi+1,column_count):
        counter+=1
        if int(row[r])>=x:
            break
    return counter

def top(x,xi,i):
    column=list(zip(*l))[xi]
    counter=0
    for c in range(i-1,-1,-1):
        counter+=1
        if int(column[c])>=x:
            break
    return counter

def bottom(x,xi,i):
    column=list(zip(*l))[xi]
    counter=0
    for c in range(i+1,row_count):
        counter+=1
        if int(column[c])>=x:
            break
    return counter

p2=[]   # part 2 list

for r in range(row_count):
    for c in range(column_count):
        element=int(l[r][c])
        value=top(element,c,r)*bottom(element,c,r)*left(element,c,r)*right(element,c,r)
        p2.append(value)

print(max(p2))  # part 2 solution
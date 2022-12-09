n = int(input())
l = []        #[[1,1,2], [2,2,3] ...]
for i in range(n):
    l.append([int(x) for x in input()])

def tailgate(x,y):
    #to check if x>y : tailgate logic
    #x and y are list elements : [1,1,2] [2,2,3] ...
    k=list(zip(x,y))
    for i in reversed(k):
        if i[0] > i[1]:
            return True     # swap
        elif i[0] == i[1]:
            pass            # wait till next iteration
        else:
            return False    # don't swap

for i in range(len(l)-1):   #sorting algorithm based on the qn
    if tailgate(l[i],l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]

for i in l:
    print("".join([str(x) for x in i]))

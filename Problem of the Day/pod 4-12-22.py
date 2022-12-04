n=int(input()) #number of lines
l=[] #points [(7,11)...]
for i in range(n):
    l.append(tuple(map(int,input().split())))
p=int(input()) #check point
l=dict(l)

c=0 #counter
k=p #flag

try:
    while True:
        k=l[k]   
        if k==p:
            break
        c+=1
except KeyError: #keyerror breaks the circle.
    c=-1

print(c+1)

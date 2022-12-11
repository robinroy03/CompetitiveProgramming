a, b = map(int,input().split())     # intial price day 1 2
q = int(input())                    # number of queries
l = list(map(int,input().split()))  # q space sep integers

k=[a,b]
for i in range(3,max(l)+1):
    c = 3*b + 4*a
    if i in l:
        k.append(c)
    a = b
    b = c
    
for i in k:
    if i > 1000000007:
        print(i%1000000007,end=' ')
    else:
        print(i,end=' ')

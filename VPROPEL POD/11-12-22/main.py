a, b = map(int,input().split())     # intial price day 1 2
q = int(input())                    # number of queries
l = tuple(map(int,input().split()))  # q space sep integers

print(a,b,end=' ')
for i in range(3,max(l)+1):
    c = 3*b + 4*a
    if i in l:
        print(c%1000000007,end=' ')
    a, b = b, c

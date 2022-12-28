w = input()
n = int(input())

l1 = ([x for x in w]*(n//len(w)+2*n))[:n]
i1 = list(range(1,n+1))

one = list(reversed(list(zip(l1,i1))))

l2 = ([x for x in w]*(n//len(w)+2*n))[n:2*n]
i2 = list(range(n,0,-1))

two = list(zip(l2,i2))

flag = 0
for i in one:
    for j in two:
        if i == j:
            print(j[1])
            flag = 1
            break
    if flag == 1:
        break
else:
    print(-1)

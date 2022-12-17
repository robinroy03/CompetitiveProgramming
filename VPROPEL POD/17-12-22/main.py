n = int(input())
l = list(map(int,input().split()))

for i in range(2,min(l)+1):
    for j in l:
        if j%i != 0:
            break
    else:
        print("YES")
        break
else:
    print("NO")

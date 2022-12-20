n = int(input())
l = []

def tri(a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)>b:
        return True
    return False

for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if i+j+k==n and not tri(i,j,k):
                l.append(tuple(sorted((i,j,k))))

print(len(set(l)))

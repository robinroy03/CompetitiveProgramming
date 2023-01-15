n = int(input())
l = list(map(int,input().split()))

storage = []

for i in range(len(l)+1):
    for j in range(i+1, len(l)+1):
        temp = l[i:j]
        if sorted(temp) == temp and len(set(temp)) == len(temp):
            storage.append([l[i:j],i+1,j])

a = (max(storage, key = lambda x: len(x[0])))

print(a[1],a[2])
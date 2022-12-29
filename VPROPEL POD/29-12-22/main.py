m = int(input())
n = int(input())

def dominant(x):
    l = []
    for i in range(1,x//2+1):
        if x%i == 0:
            l.append(i)
    return l

k = sum(dominant(m))
j = sum(dominant(n))

if k > j:
    print(m)
elif j > k:
    print(n)
else:
    print("No dominance")

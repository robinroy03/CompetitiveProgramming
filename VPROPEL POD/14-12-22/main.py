l = [int(input()) for _ in range(int(input()))]
m = int(input())
k = [x for x in l if x%m==0]

if k:
    print(min(k))
else:
    print("No multiple found")

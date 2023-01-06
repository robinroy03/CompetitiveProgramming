import math

k = int(input())
n = 0

for i in range(1,k+1):
    if math.factorial(i) == k:
        n = i
        break
else:
    print(-1)
    
if n != 0:
    sum = 1
    if n%2 == 0:
        for i in range(n,1,-2):
            sum *= i
    else:
        for i in range(n,1,-2):
            sum *= i
    print(sum)

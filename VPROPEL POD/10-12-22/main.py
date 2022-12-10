n = int(input())  # n many elements are being given
l = []            # list storing the n elements : [1, 2, 3, ... ]

for _ in range(n):  # accepting inputs from system
    l.append(int(input()))

def big_factor(x):      # function to find the biggest factor excluding the number
    max = 0
    for i in range(1,x//2+1):
        if x%i == 0:
            max = i
    return max

big = []          # storing the big factors
for i in l:     # appending to the list
    big.append(big_factor(i))

k = list(zip(big,l))      # using zip to mix both number and biggest factor
                        # [(12,6), (6,3), ... ]

for i in range(len(k)): # checking the logic, and printing the numbers that satisfy
    if k[i:][0][0] >= max(k[i:])[0]:
        print(k[i:][0][1])

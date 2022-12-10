n = int(input())
l = [int(input()) for _ in range(n)]      # taking inputs from system

def big_factor(x):      # function to find the biggest factor excluding the number
    for i in range(x//2,0,-1):
        if x%i == 0:
            return i

big = [big_factor(i) for i in l]          # storing the big factors

for i in range(n): # checking the logic, and printing the numbers that satisfy
    if big[i:][0] >= max(big[i:]):
        print(l[i:][0])

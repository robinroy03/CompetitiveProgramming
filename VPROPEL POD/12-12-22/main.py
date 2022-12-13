from itertools import repeat
from math import factorial

l = [int(input()) for i in range(int(input()))]

for i in l:
    initial = list(repeat(1,i))     # initial 1 filled list
    value = 1
    while initial.count(1) >= 2:
        initial.remove(1)
        initial.remove(1)
        initial.append(2)
        value = value + (factorial(len(initial))//(factorial(initial.count(1))*factorial(initial.count(2))))
    print(value % (10**9+7))

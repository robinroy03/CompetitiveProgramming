n = int(input())  # number of elements in the series 
s1 = [int(input()) for _ in range(n)]     # all s1 elements
s2 = [int(input()) for _ in range(n)]     # all s2 elements
xor = [int(input()) for _ in range(n)]    # all xor(s1,s2) elements

error = 0                                 # sum of error
real = []                                 # the list of real s2 elements

for i in zip(s1,xor,s2):
    value = i[0]^i[1]
    real.append(value)
    error += abs(value - i[2])

print(*real,sep = "\n")
print(error)

"""
What this program really is :

Basically 3 values were transmitted, s1 s2 and xor - but s2 got corrupted. 
We're given a WRONG CORRUPTED_s2. We're required to find the REAL_s2. 
We do it using bitwise XOR operator (^ in python).
So s1^xor gives us the REAL_s2.
Now we compare the REAL_s2 value with the CORRUPTED_s2 and get the absolute error.
Then we just print.

That's about it :)
"""

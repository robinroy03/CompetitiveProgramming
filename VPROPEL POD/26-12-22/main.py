w = input()         # the word given to Ramu
k = int(input())    # vowel count
l = []              # list to store all substrings

def vowel(x):
    """To find vowel count of x"""
    count = 0
    for i in x:
        if i in ('a','e','i','o','u'):
            count += 1
    return count

for i in range(len(w)+1):   # developing all substrings of the word
    for j in range(i):
        l.append(w[j:i])

c = 0                       # counter for final output
for i in l:
    if vowel(i) == k:
        c += 1

print(c) 

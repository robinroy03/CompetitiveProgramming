s1 = input()
s2 = input().zfill(len(s1))

res = ""

for x, y in zip(s1, s2):
    i, j = ord(x), ord(y)
    if y == '0':
        res += x
    elif (i - j) == 0:
        res += x
    elif (i - j) > 0:
        res += chr(96 + (i-j))
    else:
        res += chr(123 + (i-j))
        
print(res)

s = input()
n = int(input())
l = [s[i:i+n] for i in range(len(s)-n+1)]

for i in l:
    if 'a' not in i and 'e' not in i  and 'i' not in i and 'o' not in i and 'u' not in i:
        print(i)

n=input()
a=0
b=0
for i in range(len(n)):
    if i%2==0:
        a+=int(n[i])
    else:
        b+=int(n[i])

print(abs(b-a))

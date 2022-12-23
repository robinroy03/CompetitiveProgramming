from string import ascii_lowercase,ascii_uppercase
alphabets=[' ',*ascii_lowercase,*ascii_uppercase]

f=open("input3.txt",'r')
l=f.readlines()
f.close()

sum=0

for i in l:
    i=i.rstrip()
    part1=i[:len(i)//2]
    part2=i[len(i)//2:]
    temp=[]
    for i in part1:
        for j in part2:
            if i==j and i not in temp:
                temp.append(i)
                sum+=(alphabets.index(i))
                break

print(sum)      # part 1

# ------ part 2 below --------

sum_2=0

def duplicate(a,b,c):
    temp=[]
    for i in a:
        for j in b:
            for k in c:
                if i==j==k and i not in temp:
                    return (alphabets.index(i))

for i in range(0,len(l),3):
    a,b,c=l[i].rstrip(),l[i+1].rstrip(),l[i+2].rstrip()
    sum_2+=duplicate(a,b,c)

print(sum_2)    # part 2
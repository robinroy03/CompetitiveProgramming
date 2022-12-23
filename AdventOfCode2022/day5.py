import copy

# hardcoding the dictionary

d={1:['s','m','r','n','w','j','v','t'],
    2:['b','w','d','j','q','p','c','v'],
    3:['b','j','f','h','d','r','p'],
    4:['f','r','p','b','m','n','d'],
    5:['h','v','r','p','t','b'],
    6:['c','b','p','t'],
    7:['b','j','r','p','l'],
    8:['n','c','s','l','t','z','b','w'],
    9:['l','s','g']
}


d2=copy.deepcopy(d) # for part 2

f=open("day5_input.txt",'r')
l=f.readlines()
f.close()

def instructions(line):
    cmd=line.rstrip().split()
    count,fro,to=int(cmd[1]),int(cmd[3]),int(cmd[5])
    for i in range(count):
        d[to].append(d[fro].pop())

for line in l:
    instructions(line)

for i in d:
    print(d[i][-1],end="")  # part 1
print()

# ---- part 2 begins ---- 

def instructions_2(line):
    cmd=line.rstrip().split()
    count,fro,to=int(cmd[1]),int(cmd[3]),int(cmd[5])
    temp=[]
    for i in range(count):
        temp.append(d2[fro].pop())
    d2[to].extend(reversed(temp))

for line in l:
    instructions_2(line)

for i in d:
    print(d2[i][-1],end="") # part 2
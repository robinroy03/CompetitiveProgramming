# disclaimer : this is an extremely unoptimized hacky code, it "works".

from collections import defaultdict

n = input().split()
n = list(dict.fromkeys(n))

v_primary = []

def order(x):
    v = ['a', 'e', 'i', 'o', 'u']
    temp = [i for i in x if i in v]
    for i in range(len(temp)-1):
        if v.index(temp[i]) > v.index(temp[i+1]):
            return False
    else:
        return True
    
def no_rep(x):
    v = ['a', 'e', 'i', 'o', 'u']
    l = [x.index(i) for i in v if i in x]
    temp = [i for i in x if i in v]
    
    for i in range(len(temp)-1):
        if v.index(temp[i]) > v.index(temp[i+1]):
            return False
    if sorted(l) == l:
        return True   
    else:
        return False  
        
for i in n:
    if order(i) and no_rep(i):
        v_primary.append(i)

res = defaultdict(lambda : [])


for i in v_primary:
    temp = 0
    if 'a' in i:
        temp += 1
    if 'e' in i:
        temp += 1
    if 'i' in i:
        temp += 1
    if 'o' in i:
        temp += 1
    if 'u' in i:
        temp += 1
    res[temp].append(i)

if not res:
    print(-1)
else:
    sol = res[max(res)]

    for i in n:
        if i in sol:
            print(i)

a=int(input())
factors=[x for x in range(1,a//2+1) if a%x==0]
factors.append(a)
pair=[]
for i in factors:
    for j in factors:
        if i*j==a and ((j,i) not in pair) and ((i,j) not in pair) and i!=j:
            pair.append((i,j))
print(len(pair))

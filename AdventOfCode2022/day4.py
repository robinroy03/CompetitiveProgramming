f=open("input4.txt",'r')
l=f.readlines()
f.close()

count=0
count_2=0

for i in l:
    i=i.rstrip().split(",")
    range_1=list(map(int,i[0].split("-")))
    range_2=list(map(int,i[1].split("-")))

    a={x for x in range(range_1[0],range_1[1]+1)}
    b={x for x in range(range_2[0],range_2[1]+1)}

    if a.union(b)==a or b.union(a)==b:
        count+=1
    elif len(a.intersection(b))!=0:
        count_2+=1
print(count)    # part 1

print(count_2+count)    # part 2

n = int(input())

def divisor(x):
    """returns the count of factors of x"""
    
    if x == 1:
        return 2
    count = 0
    for i in range(1,x+1):
        if x%i == 0:
            count += 1
    return count

l = [x for x in range(1,n+1) if n%x == 0]       # list of all factors of main number
k = [divisor(x) for x in l]                     # list of "count" of factors of factors of main number
j = list(zip(k,l))                              # list with 0 as count and 1 as name


d={x[0]:[i[1] for i in j if i[0]==x[0]] for x in j}     # key is number of factors, value is digits with those many factors

count = 0
flag = 0

for key in d:
    if len(d[key]) >= 2:
        flag = 1
        for x in d[key][:len(d[key])//2]:
            for y in d[key][len(d[key])//2:]:
                if x != y and x*y == n:
                    count += 1
if flag == 1:
    print(count)
else:
    print(-1)

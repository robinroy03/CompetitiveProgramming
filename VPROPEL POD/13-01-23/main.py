n = int(input()) # number of files
m = int(input()) # edges in the file system
l=[]   
for _ in range(m):
    l.append(list(map(int,input().split())))
files = [x for x in input().split()]
di = {x:[] for x in files if "." not in x}

for i in l:
    x,y = i

    x = files[x-1]
    y = files[y-1]
    
    di[x].append(y)

q = int(input())    # number of queries
for _ in range(q):
    from_,where_,file_ = input().split()
    
    from_ = from_.split("/")[-1]
    where_ = where_.split("/")[-1]
    
    if from_ == "":
        from_ = "/"
    elif where_ == "":
        where_ = "/"

    if file_ in di[where_]:
        print("no")
    else:
        print("yes")
# accepting inputs

n = int(input())
a = int(input())
b = int(input())

time = n*(min(a,b))    # time required when fastest typer is doing solo

for i in range(0,n+1):
    ta=a*i          # time required for typist 'a' to type 'i' words
    tb=b*(n-i)      # time required for typist 'b' to type '(n-i)' words
    
    temp=max(ta,tb) # new time is the time taken by slowest typist to complete
    
    if temp<time:   
        time=temp

print(time)

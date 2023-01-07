x = list(input())
y = list(input())

x1 = x.copy()
y1 = y.copy()

if y == ['0']:
    print("-1.00")
else:
    for i in x:
        if i in y1:
            x1.remove(i)
            y1.remove(i)
    
    x = "".join(x1)
    y = "".join(y1)
    
    if x == "":
        x = 1
    if y == "":
        y = 1
    if y == "0":
        print("-1.00")
    else:
        print(format(int(x)/int(y),'0.2f'))

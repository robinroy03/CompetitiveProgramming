word = input().lower()

def reduce(x):
    """function to reduce x according to the rules"""

    new,k=' ',' '       # k is used to identify a duplicate stream
    for i in word:
        if k == i or i == "*":
            continue
        else:
            if new[-1] == i:
                new=new[:-1]
                k = i   # k is activated and used to find duplicate streams
                new += "*"
            else:
                new += i
    return new[1:]

temp = reduce(word)

while temp != word:
    if temp == "*":
        break
    
    word = temp
    temp = reduce(temp)

if temp == "*":
    print(1)
else:
    print(0)

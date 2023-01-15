l = list(map(float,input().split()))
check = float(input())

main = []
for i in l:
    if 0.2<=i<=0.7:
        main.append(0)
    elif 0.71 <=i<= 1.2:
        main.append(1)
    elif 1.21 <=i<= 1.7:
        main.append(2)
    elif 1.71 <=i<= 2.2:
        main.append(3)
    elif 2.21 <=i<= 2.7:
        main.append(4)
    elif 2.71 <=i<= 3.2:
        main.append(5)
    elif 3.21 <=i<= 3.7:
        main.append(6)
    elif 3.71 <=i<= 4.2:
        main.append(7)
    elif 4.21 <=i<= 4.7:
        main.append(8)
    elif 4.71 <=i<= 5.2:
        main.append(9)

w = [1,3,1,3,1,3,1,3,1,3]

k = sum([x[0]*x[1] for x in zip(main,w)])

if k%10 == check:
    print("Yes")
else:
    print("No")
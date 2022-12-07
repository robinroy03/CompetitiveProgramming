from itertools import combinations

row, column = map(int,input().split())
matrix = []
for _ in range(row):
    matrix.append([int(x) for x in input()])
q = int(input())  # number of queries
q_dist = []
for _ in range(q):
    q_dist.append(int(input()))

coords = []   # coords of 1

x = 0
for r in matrix:
    y = 0
    for c in r:
        if c == 1:
            coords.append((x,y))
        y += 1
    x += 1

z=list(combinations(coords,2))

new_dic = []

for x,y in z:
    temp = abs(x[0]-y[0])+abs(x[1]-y[1])    # manhattan distance formula
    if temp in q_dist:
        new_dic.append(temp)

for i in q_dist:
    print(new_dic.count(i))

# --- accepting inputs from system ---

m = int(input())    # maximum prize amount
n = int(input())    # number of players
l = []              # [['A', 2], ['B', 3] ... ]

for _ in range(n):
    temp = input().split()
    l.append([temp[0], int(temp[1])])

first = int(input())    # index of the guy who caught it first - 100% prize
x = input()             # prize of the guy to be found - his name given

# --- all inputs received ---

flag = l.index(l[first])  # initial flag
perc = 100                # initial percentage

while True:
    name = l[flag-1][0]   
    to = l[flag-1][1]
    flag = to
    if name == x:
        break
    else:
        perc -= 2

print("{:.2f}".format(m*(perc/100)))

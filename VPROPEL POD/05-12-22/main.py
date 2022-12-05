# --- taking inputs from system ---

m = int(input())    # number of rows
n = int(input())    # number of columns
p = int(input())    # number 1
q = int(input())    # number 2

matrix = []

for _ in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)

l = int(input())    # lucky number

# --- all inputs received from system ---

if l == p:          # finding the opposite number to compare with
    opposite = q
else:
    opposite = p

flag = 0        # flag variable for "No winner" condition

for r in range(m):      # row iteration
    for c in range(n):  # column iteration
        if (opposite not in matrix[r]) and (opposite not in [matrix[x][c] for x in range(m)]):
            
            # if opposite not in the corresponding row and column
    
            print(r+1,c+1)
            flag = 1        
if flag == 0:
    print("No winner")

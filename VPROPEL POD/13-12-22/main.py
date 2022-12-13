nr1 = int(input())     # number of rows in m1
nc1 = int(input())     # number of columns in m1
matrix1 = [[int(i) for i in input().split()] for _ in range(nr1)]   # filling matrix1 - each element is a row eg: [[1,2,3],[4,5,6],[7,8,9]]

nr2 = int(input())     # number of rows in m2
nc2 = int(input())     # number of columns in m2
matrix2 = [[int(i) for i in input().split()] for _ in range(nr2)]   # filling matrix2 - each element is a row eg: [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = list(zip(*matrix2))   #taking the transpose of the matrix for simplifying the question

capacity = int(input())

matrix3 = []

for r in matrix1:   
    temp_row = []
    for tempr in matrix2:
        k = list(zip(r,tempr))
        c = 0
        for i in k:
            if sum(i) <= capacity:
                c += 1
        temp_row.append(c)
    matrix3.append(temp_row)

for i in matrix3:
    print(*i,sep="\t",end="\t")
    print()

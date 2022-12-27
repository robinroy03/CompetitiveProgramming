with open("day8.txt",'r') as f:
    l=f.readlines()         # elements are row

row_count=len(l)            # 99
column_count=len(l[0])-1    # 99

class matrix:   # x = tree height, xi = tree index in row, i row index
    """To locate left, right, bottom ,top elements of a matrix"""

    def left(x,xi,i):
        """
        returns True if any tree > x in left,
        x = tree height, xi = tree index in row, i row index
        """
        row=l[i]
        for r in range(xi):
            if int(row[r])>=x:
                return True
        else:
            return False

    def right(x,xi,i):
        """
        returns True if any tree > x in right,
        x = tree height, xi = tree index in row, i row index
        """
        row=l[i]
        for r in range(xi+1,row_count):
            if int(row[r])>=x:
                return True
        else:
            return False

    def top(x,xi,i):
        """
        returns True if any tree > x in top direction,
        x=tree height, xi = tree index in row, i row index
        """
        column=list(zip(*l))[xi]
        for c in range(i):
            if int(column[c])>=x:
                return True
        else:
            return False

    def bottom(x,xi,i):
        """
        returns True if any tree > x in top direction,
        x=tree height, xi = tree index in row, i row index
        """
        column=list(zip(*l))[xi]
        for c in range(i+1,column_count):
            if int(column[c])>=x:
                return True
        else:
            return False

def mixer(x,xi,i):
    return (matrix.bottom(x,xi,i)) and (matrix.top(x,xi,i)) and (matrix.left(x,xi,i)) and (matrix.right(x,xi,i))

count=0     # for part 1

for r in range(row_count):
    for c in range(column_count):
        element=int(l[r][c])
        if not mixer(element,c,r):
            count+=1

print(count)    # part 1 solution
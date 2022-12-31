with open("day9.txt",'r') as f:
    l=f.readlines()

move={
    "U":(0,1),
    "D":(0,-1),
    "L":(-1,0),
    "R":(1,0)
}

sign = lambda x : 1 if x==2 else -1     # this is for coords in tail jump  

head,tail = [0,0],[0,0]
tail_coords = set()

def tail_move(hx,hy,tx,ty):
    if hx-tx in (-1,0,1) and hy-ty in (-1,0,1):
        return False    # don't move
    else:
        if hx-tx in (2,-2):
            tail[0] += sign(hx-tx)
            tail[1] = hy
        elif hy-ty in (2,-2):
            tail[1] += sign(hy-ty)
            tail[0] = hx

for i in l:
    i = i.rstrip().split()
    dx,dy=move[i[0]]    # head movement
    for _ in range(int(i[1])):
        head[0] += dx
        head[1] += dy
        tail_move(*head,*tail)
        tail_coords.add(tuple(tail))

print(len(tail_coords))     # part 1
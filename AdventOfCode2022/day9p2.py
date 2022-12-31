# the biggest insight is the fact that now elements could do diagonal movement 

with open("day9.txt",'r') as f:
    l = f.readlines()

move={
    "U":(0,1),
    "D":(0,-1),
    "L":(-1,0),
    "R":(1,0)
}

sign = lambda x : 1 if x==2 else -1     # this is for coords in tail jump  

snake = [[0,0] for _ in range(10)]    # -1 --> head ; 0 --> tail
tail_coords = set()

def tail_move(hx,hy,tx,ty):
    if hx-tx in (-1,0,1) and hy-ty in (-1,0,1):
        return [tx,ty]    # don't move
    elif hx-tx in (-2,2) and hy-ty in (-2,2):
        return [tx+sign(hx-tx),ty+sign(hy-ty)]
    else:
        if hx-tx in (2,-2):
            return [tx+sign(hx-tx),hy]
        elif hy-ty in (2,-2):
            return [hx,ty+sign(hy-ty)]

for x in l:
    x = x.rstrip().split()
    dx,dy = move[x[0]]    # head movement
    for _ in range(int(x[1])):
        snake[-1][0] += dx
        snake[-1][1] += dy
        for i in range(8,-1,-1):
            snake[i] = tail_move(*snake[i+1],*snake[i])
        tail_coords.add(tuple(snake[0]))

print(len(tail_coords)) # part 2
t = int(input())
for _ in range(t):
    n = int(input())    # the number of cubes
    length = list(map(int,input().split()))
    prev_floor = max(length[0],length[-1])
    for _ in range(len(length)//2):
        current_floor = max(length.pop(0),length.pop(-1))
        if prev_floor >= current_floor:
            prev_floor = current_floor
        else:
            print("No")
            break
    else:
        if length:
            if prev_floor >= length[0]:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")

p=int(input()) #dimension of board (p x p)
m,n=map(int,input().split()) #initial position
num1=int(input()) #number of moves allowed
for i in range(num1):
    move=input()
    if move=='l' and n>0:
        n-=1
    elif move=='r' and n<p-1:
        n+=1
    elif move=='u' and m<p-1:
        m+=1
    elif move=='d' and m>0:
        m-=1
win_m,win_n=map(int,input().split())
if (m,n)==(win_m,win_n):
    print("Win")
else:
    print("Loss")

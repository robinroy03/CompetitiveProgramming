f=open("C:/Users/robin/Downloads/aoc/input_day2.txt",'r')
l=f.readlines()
f.close()

# rock=1, paper=2, scissors=3
# loss=0,draw=3,win=6

d={"X":1,"Y":2,"Z":3}
win={"A":"Y","B":"Z","C":"X"}
draw={"A":"X","B":"Y","C":"Z"}
loss={"A":"Z","B":"X","C":"Y"}

score=0

for i in l:
    i=i.rstrip().split()
    if i[0]=="A" and i[1]==win[i[0]]:
        score+=(6+d[i[1]])
    elif i[0]=="A" and i[1]==draw[i[0]]:
        score+=(3+d[i[1]])
    elif i[0]=="A" and i[1]==loss[i[0]]:
        score+=(0+d[i[1]])

    elif i[0]=="B" and i[1]==win[i[0]]:
        score+=(6+d[i[1]])
    elif i[0]=="B" and i[1]==draw[i[0]]:
        score+=(3+d[i[1]])
    elif i[0]=="B" and i[1]==loss[i[0]]:
        score+=(0+d[i[1]])

    elif i[0]=="C" and i[1]==win[i[0]]:
        score+=(6+d[i[1]])
    elif i[0]=="C" and i[1]==draw[i[0]]:
        score+=(3+d[i[1]])
    elif i[0]=="C" and i[1]==loss[i[0]]:
        score+=(0+d[i[1]])


print(score)

# code till now is perfect 


score_2=0

for i in l:
    i=i.rstrip().split()

    if i[1]=="X":  # loss
        if i[0]=="A":
            score_2+=3
        elif i[0]=="B":
            score_2+=1
        else:
            score_2+=2
    elif i[1]=="Y": # draw
        if i[0]=="A":
            score_2+=(1+3)
        elif i[0]=="B":
            score_2+=(2+3)
        else:
            score_2+=(3+3)
    else:           # win
        if i[0]=="A":
            score_2+=(2+6)
        elif i[0]=="B":
            score_2+=(3+6)
        else:
            score_2+=(1+6)
print(score_2)

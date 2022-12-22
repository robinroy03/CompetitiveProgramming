import string
alphabets=[' ',*string.ascii_uppercase,*string.ascii_lowercase]

n=input()   # integer
w=input()   # word
our_word='' # word after applying the logic
match=0     # number of matching alphabets

if len(n)==2*len(w):    # condition
    for i in range(0,len(n),2):
        digit=n[i]+n[i+1]
        our_word+=alphabets[int(digit)]
        
    for i in zip(our_word,w):
        if i[0]==i[1]:
            match+=1
    print(match)
else:
    print(-1)

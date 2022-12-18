s1 = input()
s2 = input()
k1 = s1.split()
k2 = s2.split()
alphabets = list(map(chr, range(97, 123)))
def alpha(x): 
    for i in range(len(s1)):
        if (not s1[i].isalpha() or not s2[i].isalpha()) and (not s1[i].isspace() and not s2[i].isspace()):
            return False
    else:
        return True
def space():
    for i in range(len(k1)):
        if len(k1[i]) != len(k2[i]):
            return False
    else:
        return True
def stepped():
    global s1,s2
    s1=s1.replace(" ","")
    s2=s2.replace(" ","")
    for i in range(len(s1)):
        if (alphabets.index(s2[i])-alphabets.index(s1[i])==i+1):
            pass
        else:
            return False
    else:
        return True

if len(s1)!=len(s2):
    print("Length different")
elif alpha(s1)==False or alpha(s2)==False:
    print("Strings contain non alphabets")
elif space()==False:
    print("Strings differ in space")
elif stepped():
    print("Strings are stepped")
else:
    print("Strings are not stepped")

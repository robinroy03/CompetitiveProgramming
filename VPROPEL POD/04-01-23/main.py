k = int(input())
m = int(input())
l = list(map(int,input().split()))

l2 = list(set(l))
l2.sort(reverse = True)
dic = {}
v = l2.copy()           # this stores the final value

for i in l2:
    if l.count(i) % (i+1) == 0:
        dic[i] = l.count(i) - (l.count(i)//(i+1)) - 1
    else:
        dic[i] = l.count(i) - ((l.count(i)//(i+1)) + 1) - 1

while len(v) < k:
    for i in l2:
        if dic[i] > 0 and len(v) < k:
            v.append(i)
            dic[i] -= 1
            
print(sum(v) + k)


"""
TL;DR

A lotta ngo people send up requests to an mnc. Multiple people from same ngo
could apparently send reqs too. 
When they send req they send how many are in the group "excluding" them.

eg: dude says 3 --> he means there are 4 people in the group including him

when 4 people say 3 --> it means 4 people "might" be from same ngo coz
when group of 4, they send 3... uhh.. got it?

If you got it you're done with understanding question.

Now you gotta relax and solve it.
"""

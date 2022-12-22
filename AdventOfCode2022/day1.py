f = open("day1.txt",'r')
l = f.read().split("\n\n")
dec = []
for i in l:
  k = map(int,input().split("\n"))
  dec.append(sum(k))

#solution 1
print(max(dec))

#solution 2
dec.sort()
print(dec[-1]+dec[-2]+dec[-3])

f.close()

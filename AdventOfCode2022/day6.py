f=open("day6.txt",'r')
stream=f.read()
f.close()
for i in range(len(stream)):
    k={stream[x] for x in range(i,i+4)}
    j={stream[x] for x in range(i,i+14)}
    if len(k)==4:
        pass
        #print(i+4)  # part 1 not printing coz part 2 working
    if len(j)==14:
        print(i+14)
        break      # break statements depends on part 1/2, i just wrote this for getting solution.

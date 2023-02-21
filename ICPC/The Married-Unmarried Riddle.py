# Question from the ICPC Amritapuri 2020 Preliminary Round
# https://codedrills.io/contests/icpc-amritapuri-2020-preliminary-round/problems/the-married-unmarried-riddle


import re
# married --> unmarried
for _ in range(int(input())):
    s = input() # the string in consideration
    if re.search("M\?*U",s) or re.search("MU",s):
        print("Yes")
    else:
        print("No")

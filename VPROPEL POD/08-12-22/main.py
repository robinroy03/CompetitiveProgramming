n=int(input())
even_digits=list(range(2,n+1,2))

#finding the lcm
def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

lcm=find_lcm(even_digits[0],even_digits[1])
for i in range(2,len(even_digits)):
    lcm=find_lcm(lcm,even_digits[i])

for i in even_digits:
    if lcm%i==0:
        pass
    else:
        print("No such number in range")
        break
else:
    if lcm<10**7:
        print(lcm)
    else:
        print("No such number in range")

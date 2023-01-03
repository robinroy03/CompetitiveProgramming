n = [x for x in input()]        # elements are digits, type-> string
desc = sorted(n,reverse=True)   # descending order sort of digits, type -> string
asc = sorted(n)                 # ascending order sort of digits, type -> string
c =- 1                          # count variable

if len(set(n)) >= 2:            # atleast 2 unique digits required
    while True:                 # can go while True because the results are confirmed 
        c += 1                  # incrementing the counter
        desc_t = int("".join(desc).ljust(3,"0"))   # receiving the descending order sorted 3-digit number 
        asc_t = int("".join(asc))                  # receiving the ascending order sorted 3-digit number
        value = desc_t - asc_t                     # value after subtraction
        if value == 495:                            
            print(c)
            break
        else:                                      # continuing the process if value != 495
            n = [x for x in str(desc_t-asc_t)]     # the new seed is the subtracted value
            desc = sorted(n,reverse=True)          # repeating the same process
            asc = sorted(n)
else:
    print("No")

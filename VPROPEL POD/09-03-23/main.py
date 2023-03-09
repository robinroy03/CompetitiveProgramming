n = input().split()

def with_c(c):
    temp = []
    for i in n:
        if c in i:
            temp.append(i)
    return temp

def vowel_count(pairs):
    for i in pairs:
        i = i.lower()
        if i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u') != 2:
            return False
    else:
        return True

main = []

for word in n:
    for letter in word:
        pairs = with_c(letter)

        if vowel_count(pairs) and len(pairs) == 2:
            main.append(pairs)
        else:
            break
    else:
        print(word)

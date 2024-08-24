croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = 0

for alphabet in croatia:
    while alphabet in word:
        word = word.replace(alphabet, " ", 1)
        count += 1
        
count += len(word.replace(" ", ""))
print(count)
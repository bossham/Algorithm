word = input()
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in word:
    if char in vowels:
        count += 1
        
print(count)
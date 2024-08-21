S = input()
alphabet = [0]*26

for char in S:
    alphabet[ord(char) - ord('a')] += 1

print(' '.join(str(count) for count in alphabet))
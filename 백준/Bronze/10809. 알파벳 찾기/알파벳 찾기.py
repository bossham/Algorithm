s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = [-1]*26

for idx, char in enumerate(s):
    if result[ord(char) - ord('a')] == -1:
        result[ord(char) - ord('a')] = idx
print(*result)
words = [input() for _ in range(5)]
max_length = 15
result = ""

for i in range(max_length):
    for word in words:
        if i < len(word):
            result += word[i]

print(result)
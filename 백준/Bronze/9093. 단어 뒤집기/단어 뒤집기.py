t = int(input())

for _ in range(t):
    s = input()
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    result = ' '.join(reversed_words)
    print(result)
numbers = [int(input()) for _ in range(10)]
remains = [num % 42 for num in numbers]

print(len(set(remains)))
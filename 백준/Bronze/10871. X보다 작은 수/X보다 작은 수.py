n, x = map(int, input().split())
a = list(map(int, input().split()))

result = [str(num) for num in a if num < x]
print(' '.join(result))
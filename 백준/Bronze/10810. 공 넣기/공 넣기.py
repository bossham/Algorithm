n, m = map(int, input().split())
baskets = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        baskets[index-1] = k
print(' '.join(map(str, baskets)))
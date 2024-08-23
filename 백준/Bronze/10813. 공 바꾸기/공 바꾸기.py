n,m = map(int, input().split())
baskets = [0] + list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]
    
print(' '.join(map(str, baskets[1:])))
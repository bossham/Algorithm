n = int(input())
times = []

for _ in range(n):
    a,b = map(int, input().split())
    
    if a <= b:
        times.append(b)
        
if not times:
    print(-1)
else:
    print(min(times))
max_p = 0
current = 0

for _ in range(4):
    off, on = map(int, input().split())
    current -= off
    current += on
    
    if current > max_p:
        max_p = current
        
print(max_p)
n = int(input())

result = 0
for i in range(1, n):
    digits_sum = sum(map(int, str(i)))
    if i + digits_sum == n:
        result = i
        break
        
print(result)
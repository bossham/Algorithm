numbers = []

for _ in range(5):
    n = int(input())
    numbers.append(n)
    
avg = sum(numbers) // 5
sort_n = numbers.sort()
med = numbers[2]

print(avg)
print(med)
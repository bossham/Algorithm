odd_numbers = []

for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        odd_numbers.append(num)
        
if odd_numbers:
    print(sum(odd_numbers))
    print(min(odd_numbers))
else:
    print(-1)
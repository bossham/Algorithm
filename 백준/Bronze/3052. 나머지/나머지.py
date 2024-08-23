remainders = set()

for _ in range(10):
    num = int(input())
    n = num % 42
    remainders.add(n)
    
print(len(remainders))
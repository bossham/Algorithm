N = int(input())
numbers = list(map(int, input().split()))
prime_count = 0

for number in numbers:
    if number > 1:  
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

print(prime_count)
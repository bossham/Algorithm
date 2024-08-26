M = int(input())
N = int(input())

primes = []

for number in range(M, N + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            primes.append(number)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)

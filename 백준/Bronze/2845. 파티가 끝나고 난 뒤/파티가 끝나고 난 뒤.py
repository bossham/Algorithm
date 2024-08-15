L, P = map(int, input().split())
people = L * P
counts = list(map(int, input().split()))

for count in counts:
    print(count - people, end= ' ')
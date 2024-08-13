A, B, C = map(int, input().split())
D = int(input())

total = A * 60 * 60 + B * 60 + C + D

A = (total // 3600) % 24
B = (total % 3600) // 60
C = total % 60

print(A, B, C)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

S = sum(a)
T = sum(b)

print(max(S, T))
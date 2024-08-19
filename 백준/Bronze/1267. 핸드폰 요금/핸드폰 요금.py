N = int(input())
times = list(map(int, input().split()))

Y_cost = sum((time // 30 + 1) * 10 for time in times)
M_cost = sum((time // 60 + 1) * 15 for time in times)

if Y_cost < M_cost:
    print(f"Y {Y_cost}")
elif M_cost < Y_cost:
    print(f"M {M_cost}")
else:
    print(f"Y M {Y_cost}")
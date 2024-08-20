N = int(input())
max_prize = 0

for _ in range(N):
    dice = list(map(int, input().split()))
    dice.sort()

    if dice[0] == dice[2]:  # 같은 눈이 3개
        prize = 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[1] == dice[2]:  # 같은 눈이 2개
        prize = 1000 + dice[1] * 100
    else:  # 모두 다른 눈
        prize = dice[2] * 100

    max_prize = max(max_prize, prize)

print(max_prize)

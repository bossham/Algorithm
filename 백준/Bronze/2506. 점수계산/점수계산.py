N = int(input())
scores = list(map(int, input().split()))

total_score = 0
current_score = 0

for score in scores:
    if score == 1:
        current_score += 1
        total_score += current_score
    else:
        current_score = 0

print(total_score)

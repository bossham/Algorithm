n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True)
k_score = scores[k-1]

print(k_score)
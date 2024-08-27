n,m = map(int, input().split())
cards = list(map(int, input().split()))
total = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = cards[i]+cards[j]+cards[k]
            if card_sum <= m:
                total = max(total, card_sum)
                
print(total)
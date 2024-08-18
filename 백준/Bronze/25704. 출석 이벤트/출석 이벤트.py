n = int(input())
price = int(input())
discounts = []

if n >= 5:
    discounts.append(500)
if n >= 10:
    discounts.append(price // 10)
if n >= 15:
    discounts.append(2000)
if n >= 20:
    discounts.append(price // 4)

max_discount = max(discounts, default=0)
final_price = max(price - max_discount, 0)
print(final_price)
X = []
Y = []

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    
for x in X:
    if X.count(x) == 1:
        x4 = x
for y in Y:
    if Y.count(y) == 1:
        y4 = y
print(x4, y4)
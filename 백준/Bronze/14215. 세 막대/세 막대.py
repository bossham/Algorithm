a, b, c = map(int, input().split())
side = sorted([a,b,c])

if side[0]+side[1] > side[2]:
    print(sum(side))
else:
    side[2] = side[0] + side[1] -1
    print(sum(side))
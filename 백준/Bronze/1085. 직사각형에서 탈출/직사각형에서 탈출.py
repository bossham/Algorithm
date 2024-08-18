x,y,w,h = map(int, input().split())

left = x
right = w-x
bottom = y
top = h-y

distance = min(left, right, bottom, top)
print(distance)
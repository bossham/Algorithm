n = int(input())
room = 1
step = 1

if n ==1:
    print(1)
else:
    while room < n:
        room += 6*step
        step += 1
    print(step)
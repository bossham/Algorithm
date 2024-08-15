times = [int(input()) for _ in range(4)]
total = sum(times)
minutes = total // 60
seconds = total % 60

print(minutes)
print(seconds)
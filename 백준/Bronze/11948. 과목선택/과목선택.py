a,b,c,d,e,f = [int(input()) for _ in range(6)]

science = [a,b,c,d]
history = [e,f]
science.sort(reverse=True)
history.sort(reverse=True)

total = sum(science[:3]) + history[0]
print(total)
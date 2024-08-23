total = set(range(1, 31))
submitted = set()

for _ in range(28):
    submitted.add(int(input()))
    
not_submitted = total - submitted

print(min(not_submitted))
print(max(not_submitted))
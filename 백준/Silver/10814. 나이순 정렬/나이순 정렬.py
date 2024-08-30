N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    members.append((int(age), i, name))

sorted_members = sorted(members)

for member in sorted_members:
    print(f"{member[0]} {member[2]}")
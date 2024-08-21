y1,m1,d1 = map(int, input().split())
y2,m2,d2 = map(int, input().split())

man_age = y2 - y1
if (m2,d2) < (m1,d1):
    man_age -= 1
    
count_age = y2 - y1 + 1
year_age = y2 - y1

print(man_age)
print(count_age)
print(year_age)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

subject = [a,b,c,d]
subject.sort(reverse=True)
subject1 = sum(subject[:3])

subject2 = max(e,f)
print(subject1+subject2)
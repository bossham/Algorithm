N = int(input())

for _ in range(N):
    str1, str2 = input().split()

    if sorted(str1) == sorted(str2):
        print('Possible')
    else:
        print('Impossible')
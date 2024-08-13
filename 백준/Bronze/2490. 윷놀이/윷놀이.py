def check_yut(yut):
    count_0 = yut.count(0)
    
    if count_0 == 1:
        return 'A'
    elif count_0 == 2:
        return 'B'
    elif count_0 == 3:
        return 'C'
    elif count_0 == 4:
        return 'D'
    else:
        return 'E'
    
for _ in range(3):
    yut = list(map(int, input().split()))
    print(check_yut(yut))
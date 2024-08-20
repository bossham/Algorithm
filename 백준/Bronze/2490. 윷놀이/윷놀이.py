for _ in range(3):
    yut = list(map(int, input().split()))
    count_0 = yut.count(0)
    
    if count_0 == 1:
        print('A')
    elif count_0 == 2:
        print('B')
    elif count_0 == 3:
        print('C')
    elif count_0 == 4:
        print('D')
    else:
        print('E')
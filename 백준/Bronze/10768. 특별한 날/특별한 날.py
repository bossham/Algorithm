M, D = [int(input()) for _ in range(2)]

if M == 2:
    if D < 18:
        print('Before')
    elif D == 18:
        print('Special')
    else:
        print('After')
elif M < 2:
    print('Before')
else:
    print('After')
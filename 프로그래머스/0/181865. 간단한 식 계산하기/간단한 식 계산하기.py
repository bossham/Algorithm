def solution(binomial):
    bino = binomial.split()
    a = int(bino[0])
    op = bino[1]
    b = int(bino[2])
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b
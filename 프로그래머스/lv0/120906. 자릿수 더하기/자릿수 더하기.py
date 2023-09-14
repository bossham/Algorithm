def solution(n):
    digits = str(n)
    
    return sum(int(digit) for digit in digits)
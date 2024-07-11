def solution(myString):
    result = ''
    for c in myString:
        if c == 'a':
            result += 'A'
        elif c != 'A' and c.isupper():
            result += c.lower()
        else:
            result += c
    return result
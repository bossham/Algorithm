def solution(myString):
    string = myString.split('x')
    result = [len(s) for s in string]
    return result
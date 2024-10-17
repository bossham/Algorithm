def solution(myString):
    answer = []
    result = myString.split('x')
    answer = [len(x) for x in result]
    return answer
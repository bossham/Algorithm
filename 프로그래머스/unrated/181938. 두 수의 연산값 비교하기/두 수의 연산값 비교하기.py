def solution(a, b):
    ab = int(str(a) + str(b))
    answer2 = 2 * int(str(a)) * int(str(b))
    
    if ab == answer2:
        return ab
    elif ab >= answer2:
        return ab
    else:
        return answer2
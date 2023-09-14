def solution(sides):
    sides.sort(reverse=True)
    if sum(sides[1:]) > sides[0]:
        return 1
    else:
        return 2
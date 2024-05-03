def solution(hp):
    a = hp // 5
    remaining_hp = hp % 5
    b = remaining_hp // 3
    c = remaining_hp % 3
    return a + b + c
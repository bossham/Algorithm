def solution(angle):
    if angle > 0 and angle < 90:
        return 1  # 예각
    elif angle == 90:
        return 2  # 직각
    elif angle > 90 and angle < 180:
        return 3  # 둔각
    elif angle == 180:
        return 4
    else:
        return -1
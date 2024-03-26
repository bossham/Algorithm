def solution(num_list):
    return [sum(x % 2 == 0 for x in num_list), sum(x % 2 != 0 for x in num_list)]
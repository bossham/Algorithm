def solution(num_list):
    result = 1
    for n in num_list:
        result *= n
        
    if result < sum(num_list)**2:
        return 1
    else:
        return 0
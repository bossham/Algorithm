def solution(num_list):
    num1 = sum(num_list[1::2])
    num2 = sum(num_list[::2])
    if num1 == num2:
        return num1
    else:
        return max(num1, num2)
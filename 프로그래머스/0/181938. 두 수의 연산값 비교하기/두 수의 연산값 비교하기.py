def solution(a, b):
    answer = 0
    str_a = str(a)
    str_b = str(b)
    answer1 = int(str_a + str_b)
    answer2 = 2*a*b
    if answer1 >= answer2:
        return answer1
    else:
        return answer2
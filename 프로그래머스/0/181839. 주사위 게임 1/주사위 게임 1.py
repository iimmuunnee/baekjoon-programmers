def solution(a, b):
    answer = 0
    a_2 = a % 2 # 0이면 짝수, 1이면 홀수
    b_2 = b % 2 # 0이면 짝수, 1이면 홀수
    
    if a_2 == 1 and b_2 == 1:
        answer = a**2 + b**2
    elif a_2 == 1 or b_2 == 1:
        answer = 2 * (a + b)
    elif a_2 == 0 and b_2 == 0:
        answer = abs(a - b)
    
    return answer
def solution(n):
    answer = 0
    a = n // 7
    b = n % 7
    if b == 0:
        answer = a
    else:
        answer = a + 1
    return answer
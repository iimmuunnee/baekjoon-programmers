def solution(n):
    answer = 0
    cnt = 2
    while True:
        if (n < factorial(cnt)):
            break
        cnt += 1
    answer = cnt - 1
    
    return answer

def factorial(number):
    sum = 1
    for i in range(2, number + 1):
        sum *= i
    
    return sum
def solution(n):
    answer = 0
    
    list_a = range(1, n + 1)
    for i in list_a:
        if n % i == 0:
            answer += 1
          
    return answer
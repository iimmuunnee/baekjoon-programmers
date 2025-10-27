def solution(arr):
    answer = arr
    n = 1
    while len(arr) > n:
        n *= 2
    
    while len(answer) != n:
        answer.append(0)
    
    return answer
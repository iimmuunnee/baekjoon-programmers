def solution(a, d, included):
    answer = 0
    n = len(included)
    
    for i in range(n):
        if included[i]:
            answer += a + i * d
    
    return answer
def solution(s1, s2):
    answer = 0
    n = len(s1)
    for x in range(0, n):
        if s1[x] in s2:
            answer += 1
    
    return answer
def solution(k, m, score):
    answer = 0
    sscore = sorted(score, reverse=True)
    if m > len(sscore):
        return 0
    for i in range(m - 1, len(sscore), m):
        answer += sscore[i] * m
    return answer
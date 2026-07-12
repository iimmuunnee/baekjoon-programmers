def solution(land):
    for i in range(1, len(land)):
        prev = land[i-1]
        for j in range(4):
            land[i][j] += max(prev[:j] + prev[j+1:])
    return max(land[-1])
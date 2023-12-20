import math
def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1): # i : x = 1, x = 2 ...
        if i < r1: # 작은 원을 지날 때 y좌표 시작
            s = math.ceil(math.sqrt(r1**2 - i**2))
        else:
            s = 0
        # e : 끝 y좌표
        e = int(math.sqrt(r2**2 - i**2))
        answer += e - s + 1
    
    return answer*4
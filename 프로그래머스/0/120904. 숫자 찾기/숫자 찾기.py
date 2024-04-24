def solution(num, k):
    answer = 0
    if str(num).find(str(k)) == -1:
        answer = -1
    else:
        answer = str(num).find(str(k)) + 1
    return answer
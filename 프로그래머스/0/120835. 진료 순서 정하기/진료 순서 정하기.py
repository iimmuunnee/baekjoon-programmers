def solution(emergency):
    answer = [0] * len(emergency)
    sort_emergency = sorted(emergency, reverse = True)
    num = 1
    for i in sort_emergency:
        answer[emergency.index(i)] = num
        num += 1
    return answer
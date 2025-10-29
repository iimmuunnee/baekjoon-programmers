def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        bool_05 = True
        for c in str(i):
            if c not in ['0', '5']:
                bool_05 = False
                break
        if bool_05:
            answer.append(int(i))
    if len(answer) == 0:
        answer = [-1]
    return answer
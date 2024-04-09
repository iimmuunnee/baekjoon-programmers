from math import ceil
def solution(progresses, speeds):
    d_day = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    cnt = 1
    answer = []
    for i in range(len(d_day)):
        try:
            if d_day[i] < d_day[i + 1]:
                answer.append(cnt)
                cnt = 1
            else:
                d_day[i + 1] = d_day[i]
                cnt += 1
        except:
            answer.append(cnt)
            
    return answer
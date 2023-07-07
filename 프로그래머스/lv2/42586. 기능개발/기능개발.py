def solution(progresses, speeds):
    d_day = [] # 5 10 1 1 20 1
    cnt = 0
    biggest = 0
    answer = []

    len_list = len(speeds) # 3

    for i in range(len_list):
        if (100 - progresses[i]) % speeds[i] != 0:
            left_pro = (100 - progresses[i]) // speeds[i] + 1
            d_day.append(left_pro)
        else:
            left_pro = (100 - progresses[i]) // speeds[i]
            d_day.append(left_pro)

    biggest = d_day[0]

    for i in range(len_list): # 0 1 2
        if biggest >= d_day[i]:
            cnt += 1
            if i == len_list - 1:
                answer.append(cnt)
        elif biggest < d_day[i]:
            answer.append(cnt)
            biggest = d_day[i]
            cnt = 1
            if i == len_list - 1:
                answer.append(cnt)
    return answer
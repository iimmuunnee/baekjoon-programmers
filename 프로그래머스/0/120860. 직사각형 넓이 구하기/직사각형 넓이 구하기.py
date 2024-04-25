def solution(dots):
    answer = 0
    x_list = []
    y_list = []
    for i in dots:
        x_list.append(i[0])
        y_list.append(i[1])
    answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
    return answer
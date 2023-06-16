def solution(num_list):
    answer = []
    a_list = []
    b_list = []
    for a in num_list:
        if a % 2 == 0:
            a_list.append(a)
        else:
            b_list.append(a)
    a_num = len(a_list)
    b_num = len(b_list)
    c_list =[]
    c_list.append(a_num)
    c_list.append(b_num)
    answer.extend(c_list)
        
    return answer
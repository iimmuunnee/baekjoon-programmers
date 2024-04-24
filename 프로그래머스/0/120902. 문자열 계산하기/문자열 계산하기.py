def solution(my_string):
    answer = 0
    str_list = my_string.split(" ")
    for idx in range(0, len(str_list), 2):
        if idx == 0:
            answer += int(str_list[idx])
        else:
            if str_list[idx - 1] == "+":
                answer += int(str_list[idx])
            elif str_list[idx - 1] == "-":
                answer -= int(str_list[idx])
        
        
    return answer
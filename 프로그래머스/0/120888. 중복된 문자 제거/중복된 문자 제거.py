def solution(my_string):
    # str_list = my_string.split(" ")
    str_list = []
    for i in my_string:
        if i not in str_list:
            str_list.append(i)  
    answer = "".join(str_list)
    return answer
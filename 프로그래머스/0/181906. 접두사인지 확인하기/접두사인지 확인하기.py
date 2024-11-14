def solution(my_string, is_prefix):
    answer = 1
    len_word = 0
    if len(my_string) >= len(is_prefix):
        len_word = len(is_prefix)
    else:
        answer = 0
        return answer
        
    for i in range(len_word):
        if my_string[i] != is_prefix[i]:
            answer = 0
            break
            
    return answer
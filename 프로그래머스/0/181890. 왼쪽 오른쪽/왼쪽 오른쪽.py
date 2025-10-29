def solution(str_list):
    answer = []
    
    if "l" not in str_list and "r" not in str_list:
        return []
    
    for i, v in enumerate(str_list):
        if v == "l":
            answer = str_list[:i]
            break
        elif v == "r":
            answer = str_list[i+1:]
            break
            
    return answer
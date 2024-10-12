def solution(arr1, arr2):
    answer = 0
    len_arr1, len_arr2 = len(arr1), len(arr2)
    
    if len_arr1 > len_arr2:
        answer = 1
    elif len_arr1 < len_arr2:
        answer = -1
    elif len_arr1 == len_arr2:
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1
        elif sum(arr1) == sum(arr2):
            answer = 0
    
    return answer
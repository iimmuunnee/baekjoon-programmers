def solution(myString, pat):
    answer = 0
    str_arr = list(myString)
    for idx, i in enumerate(str_arr):
        if i == "A":
            str_arr[idx] = "B"
        elif i == "B":
            str_arr[idx] = "A"
    myString = ''.join(str_arr)
            
    if pat in myString:
        answer = 1
    else:
        answer = 0
        
    return answer
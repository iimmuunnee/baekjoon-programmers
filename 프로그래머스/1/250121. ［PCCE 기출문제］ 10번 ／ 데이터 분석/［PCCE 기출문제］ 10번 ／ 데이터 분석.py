def solution(data, ext, val_ext, sort_by):
    answer = []
    number = -1 # ext num
    n = len(data) # data 길이
    
    if ext == "code":
        number = 0
    elif ext == "date":
        number = 1
    elif ext == "maximum":
        number = 2
    elif ext == "remain":
        number = 3
    else :
        number = -1
        
    for i in range(n):
        if data[i][number] < val_ext:
            answer.append(data[i])
    
    if sort_by == "code":
        number = 0
    elif sort_by == "date":
        number = 1
    elif sort_by == "maximum":
        number = 2
    elif sort_by == "remain":
        number = 3
    else :
        number = -1
        
    answer.sort(key=lambda x:x[number])
        
    return answer
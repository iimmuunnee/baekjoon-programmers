def solution(arr, idx):
    answer = 0
    
    for index, value in enumerate(arr):
        if index >= idx:
            if value == 1:
                return index
            else:
                answer = -1
                
    return answer
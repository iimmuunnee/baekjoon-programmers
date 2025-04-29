def solution(arr, flag):
    answer = []
    
    for idx, boolean in enumerate(flag):
        if boolean:
            answer.extend([arr[idx]] * (arr[idx] * 2))
        else:
            answer = answer[:-arr[idx]]
            
    return answer
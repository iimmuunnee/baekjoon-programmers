def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        arr_slice = list(item for item in arr[s:e+1] if item > k)
        
        if len(arr_slice) > 0:
            answer.append(min(arr_slice))
        else:
            answer.append(-1)
        
    return answer
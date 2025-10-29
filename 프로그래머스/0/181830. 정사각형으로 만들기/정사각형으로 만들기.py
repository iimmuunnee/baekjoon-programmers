def solution(arr):
    answer = [[]]
    x, y = len(arr), len(arr[0]) # 행, 열
    diff = x - y
    if diff > 0: # 행이 더 클 때
        for i in range(x):
            for _ in range(diff):
                arr[i].append(0)
    elif diff < 0: # 열이 더 클 때
        print("열이 더 큼")
        for _ in range(abs(diff)):
            arr.append([0] * y)        
        
        
    return arr
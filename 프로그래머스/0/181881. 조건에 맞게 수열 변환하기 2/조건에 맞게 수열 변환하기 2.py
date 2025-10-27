def solution(arr):
    answer = 0
    temp = arr.copy()
    next_arr = arr.copy()
    while True:
        for i, v in enumerate(next_arr):
            if v >= 50 and v % 2 == 0:
                next_arr[i] //= 2
            elif v < 50 and v % 2 == 1:
                next_arr[i] *= 2
                next_arr[i] += 1
        if temp == next_arr:
            break
        else:
            temp = next_arr.copy()
            answer += 1
                
    return answer
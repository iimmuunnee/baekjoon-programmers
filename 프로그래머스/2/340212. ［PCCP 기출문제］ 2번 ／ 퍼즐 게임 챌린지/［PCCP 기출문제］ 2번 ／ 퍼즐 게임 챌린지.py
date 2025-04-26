# diffs > level 일 때 (time_cur + time_prev) * (diffs - level) + time_cur
# diffs <= level 일 때 time_cur

def solution(diffs, times, limit):
    answer = -1 # 최솟값
    left = 1
    right = max(diffs)

    while (left <= right):
        mid = (left + right) // 2
        total = total_time(diffs, times, mid)
        
        if total <= limit:
            answer = mid
            right = mid - 1
            
        else:
            left = mid + 1
        
    return answer

def total_time (diffs, times, level):
    total = 0
    
    for i in range(len(diffs)):
        time_cur = times[i]
        time_prev = times[i - 1] if i > 0 else 0
        
        if diffs[i] <= level:
            total += times[i]
        else:
            total += (time_cur + time_prev) * (diffs[i] - level) + time_cur
            
    return total
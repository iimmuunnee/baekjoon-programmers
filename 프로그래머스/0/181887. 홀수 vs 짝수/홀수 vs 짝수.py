def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    n = len(num_list)
    for i in range(0, n, 2):
        odd += num_list[i]
    for i in range(1, n, 2):
        even += num_list[i]
    if odd >= even:
        answer = odd    
    else:
        answer = even
    return answer
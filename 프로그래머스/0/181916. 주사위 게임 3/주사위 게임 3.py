def solution(a, b, c, d):
    answer = 0
    dice_list = [a, b, c, d]
    dice_cnt = {}
    for n in dice_list:
        if n not in dice_cnt:
            dice_cnt[n] = 1
        else:
            dice_cnt[n] += 1
    n = len(dice_cnt)
    sorted_dict = sorted(dice_cnt.items(), reverse=True ,key=lambda item: item[1])
    
    if n == 1: # 모두 같을 때:
        answer += 1111 * sorted_dict[0][0]
    elif n == 2:
        if sorted_dict[0][1] == 3: # 3개 같고 1개 다름
            p = sorted_dict[0][0]
            q = sorted_dict[1][0]
            answer += (10 * p + q) ** 2
        else:
            p = sorted_dict[0][0]
            q = sorted_dict[1][0]
            answer += (p + q) * abs(p - q)
    elif n == 3:
        q = sorted_dict[1][0]
        r = sorted_dict[2][0]
        answer += q * r
    elif n == 4:
        answer += min(sorted_dict, key=lambda x: x[0])[0]
    
    return answer
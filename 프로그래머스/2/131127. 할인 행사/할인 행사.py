def solution(want, number, discount):
    answer = 0
    discount_day = len(discount)
    want_n = sum(number)
    for i in range(discount_day - want_n + 1):
        dis_list = discount[i:i+want_n]
        dis_bool = True
        for i, v in enumerate(want):
            if number[i] != dis_list.count(v):
                dis_bool = False
                break
        if dis_bool:
            answer += 1
            
    return answer
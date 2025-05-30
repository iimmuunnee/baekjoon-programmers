def solution(wallet, bill):
    answer = 0 # 카운트
    while(min(bill[0], bill[1]) > min(wallet[0], wallet[1]) or max(bill[0], bill[1]) > max(wallet[0], wallet[1])):
        if (bill[0] > bill[1]):
            bill[0] //= 2
        elif (bill[0] < bill[1]):
            bill[1] //= 2
        answer += 1
    return answer
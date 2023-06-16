def solution(money):
    answer = []
    if money - 5500 >= 0:
        a = money // 5500 #살 수 있는 커피 잔 수
        b = money - (a * 5500) #잔돈
        answer.extend([a, b])
    else:
        answer.extend([0, money])
    return answer
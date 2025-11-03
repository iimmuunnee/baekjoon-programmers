def solution(num, total):
    answer = []
    offset = num * (num - 1) // 2
    # 초항
    a = (total - offset) // num
    answer = [a + i for i in range(num)]
    return answer
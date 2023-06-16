def solution(n, k):
    answer = 0
    real_k = k - int(n/10)
    price = 12000 * n + 2000 * real_k
    answer = price
    return answer
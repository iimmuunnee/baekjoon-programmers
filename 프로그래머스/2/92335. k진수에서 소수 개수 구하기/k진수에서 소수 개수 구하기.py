import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    # 10진수 -> k진수
    if n == 0:
        return 0
    rev_base = []
    while n > 0:
        n, mod = divmod(n, k)
        rev_base.append(str(mod))
    base_k = ''.join(rev_base[::-1])

    # 0을 기준으로 분리한 조각들 중 숫자로 바꿔 소수인지 확인
    for chunk in base_k.split('0'):
        if not chunk:        # 빈 문자열 skip
            continue
        val = int(chunk)     # <-- 문자열을 정수로
        if is_prime(val):
            answer += 1

    return answer

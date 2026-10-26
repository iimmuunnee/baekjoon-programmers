def convert(num, n):
    if num == 0:
        return "0"
    hexa = "0123456789ABCDEF"
    result = ""
    while num > 0:
        result = hexa[num % n] + result   # 나머지를 앞에 붙이면 뒤집을 필요 없음
        num //= n
    return result

def solution(n, t, m, p):
    s = ""
    num = 0
    while len(s) < t * m:
        s += convert(num, n)
        num += 1
        
    return s[p - 1 :: m][:t]
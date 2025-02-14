import sys
import math

input = sys.stdin.readline

def min_squares(n):
    # 1개
    if math.isqrt(n) ** 2 == n:
        return 1

    # 2개
    for i in range(1, math.isqrt(n) + 1):
        if math.isqrt(n-i**2) ** 2 == n - i**2:
            return 2
        
    # 4개 르장드르의 삼제곱 정리 n = 4^a(8b + 7)
    temp = n
    while temp % 4 == 0:
        temp //= 4
    if temp % 8 == 7:
        return 4
    
    return 3

n = int(input().strip())
sys.stdout.write(f"{min_squares(n)}")
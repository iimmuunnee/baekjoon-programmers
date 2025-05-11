import sys
from math import gcd

print = sys.stdout.write

t = int(sys.stdin.readline()) # 테스트 데이터 개수
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

def lcm(a, b):
    return a * b // gcd(a, b)

for M, N, x, y in arr:
    k = x
    max_k = lcm(M, N)
    find = False

    # k = x (mod M)
    # k = y (mod N)
    # x는 항상 만족한다고 가정
    while k <= max_k:
        if (k - y) % N == 0:
            print(str(k) + "\n")
            find = True
            break
        k += M

    if not find:
        print("-1\n")
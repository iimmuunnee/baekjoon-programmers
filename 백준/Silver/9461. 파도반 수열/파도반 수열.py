import sys

input = sys.stdin.readline

t = int(input().strip()) # 테스트 케이스 개수

def triangle (n):
    side = [1, 1, 1, 2, 2]
    if n > 5:
        for i in range(5, n + 1):
            side.append(side[i-1] + side[i-5])
        return side[n-1]
    else:
        return side[n-1]



for _ in range(t):
    n = int(input().strip())
    result = triangle(n)
    sys.stdout.write(f"{result}\n")
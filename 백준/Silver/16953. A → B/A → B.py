import sys

input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 0

while b > a:
    if b % 10 == 1: # 1로 끝남
        b //= 10
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        cnt = -1 # 홀수이면서 1로 끝나지않는경우는 있을 수 없음
        break

if a == b and cnt != -1:
    print(cnt + 1)
else:
    print(-1)

import sys

input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    closet = {}
    n = int(input()) # 의상이름 의상종류의 개수
    for _ in range(n):
        clothes, clothes_type = input().rstrip().split()
        closet.setdefault(clothes_type, []).append(clothes)

    result = 1 # 경우의 수 구할 때 (종류의 의상 수의 곱)-1 이라 0이면 곱의 의미가 없음

    for c in closet.values():
        result *= (len(c) + 1) # 1은 그 종류를 아무것도 안 입는 경우
    result -= 1 # 모두 안 입어서 알몸인 경우를 제외

    sys.stdout.write(f"{result}\n")
    
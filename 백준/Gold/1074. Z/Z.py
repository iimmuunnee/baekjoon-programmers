import sys

# 0행 0열 부터 시작임

def z(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    area = half * half

    if r < half and c < half:
        # 컴퓨터 1사분면 (왼쪽 위)
        return z(n - 1, r, c)
    elif r < half and c >= half:
        # 2사분면 (오른쪽 위)
        return area + z(n - 1, r, c - half) # area + : 1사분면의 면적을 이미 지났다고 치고 / c - half : 분할된 사분면 안에서의 새로운 좌표?라고 이해하기
    elif r >= half and c < half:
        # 3사분면면 (왼쪽 아래)
        return area * 2 + z(n - 1, r - half, c)
    elif r >= half and c >= half:
        # 4사분면 (오른쪽 아래)
        return area * 3 + z(n - 1, r - half, c - half)

n, r, c = map(int, sys.stdin.readline().split())
sys.stdout.write(str(z(n, r, c)))

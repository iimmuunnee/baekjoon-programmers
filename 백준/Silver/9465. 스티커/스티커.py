import sys

input = sys.stdin.readline

def sticker(n, case):
    # 각 열에서 1행을 고르거나, 2행을 고르거나, 아무것도 안 고르거나. 3가지 선택지
    dp = [[0] * n for _ in range(3)]
    dp[0][0] = case[0][0]
    dp[1][0] = case[1][0]
    dp[2][0] = 0

    for i in range(1, n):
        # 1행을 고를 때 -> 그 전에 2행 or 아무것도 안 고름
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + case[0][i]
        # 2행을 고를 때 -> 그 전에 1행 or 아무것도 안 고름
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + case[1][i]
        # 아무것도 안 고를 때 -> 그 전에 1행 or 2행
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])

    return max(dp[0][n-1], dp[1][n-1], dp[2][n-1])

t = int(input())

for _ in range(t):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(2)]
    
    print(sticker(n, case))
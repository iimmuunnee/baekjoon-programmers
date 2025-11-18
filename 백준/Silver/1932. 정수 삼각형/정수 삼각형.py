import sys

input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = tri[0][0] # 맨 위

for i in range(1, n):
    for j in range(i + 1): # j가 0이면 맨 왼쪽, i면 맨 오른쪽
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j] # 이전 위치 + 지금 위치 
        elif j == i:
            dp[i][j] = dp[i-1][i-1] + tri[i][j]
        else: # 0 < j < i
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[n-1]))
        
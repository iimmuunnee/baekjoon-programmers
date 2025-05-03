import sys

n = int(sys.stdin.readline()) # 집의 수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = cost[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

sys.stdout.write(str(min(dp[n-1])))
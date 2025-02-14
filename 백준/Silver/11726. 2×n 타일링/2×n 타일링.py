import sys
import math

input = sys.stdin.readline

n = int(input().rstrip()) # 가로 길이

dp = [0] * (n + 1)
dp[1] = 1
if n >= 2:
    dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10_007

print(dp[n])

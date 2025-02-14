import sys

input = sys.stdin.readline

n = int(input().rstrip()) # 가로길이

dp = [0] * (n + 1)

dp[1] = 1

if n >= 2:
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + 2*dp[i-2]) % 10_007

sys.stdout.write(f"{dp[n]}")

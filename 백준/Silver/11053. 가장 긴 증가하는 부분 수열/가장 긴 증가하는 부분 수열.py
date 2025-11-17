import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if n_list[j] < n_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
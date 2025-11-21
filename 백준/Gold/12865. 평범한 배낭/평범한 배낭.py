import sys

input = sys.stdin.readline

# dp
n, k = map(int, input().split())

dp = [0] * (k + 1)

thing = []
for _ in range(n):
    w, v = map(int, input().split())
    thing.append((w, v))

for w, v in thing:
    for cap in range(k, w - 1, -1): # 7 6 5 4
        dp[cap] = max(dp[cap], dp[cap - w] + v)
        
print(max(dp))
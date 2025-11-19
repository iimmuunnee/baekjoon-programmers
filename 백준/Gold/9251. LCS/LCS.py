import sys

input = sys.stdin.readline
a = input().strip()
b = input().strip()
n_a = len(a)
n_b = len(b)
dp = [[0] * (n_b + 1)]

for _ in range(n_a):
    row = [0] + ["-" for _ in range(n_b)]
    dp.append(row)

for i in range(1, n_a + 1): # A 인덱스
    for j in range(1, n_b + 1): # B 인덱스
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        elif a[i - 1] != b[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
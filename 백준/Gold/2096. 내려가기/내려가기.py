import sys

input = sys.stdin.readline

n = int(input()) # n줄에 3개씩
a0, a1, a2 = map(int, input().split()) # 가장 윗줄 값
max_dp = [a0, a1, a2]
min_dp = [a0, a1, a2]

for _ in range(n - 1): # 2행부터
    b0, b1, b2 = map(int, input().split())

    new_max0 = max(max_dp[0], max_dp[1]) + b0
    new_max1 = max(max_dp[0], max_dp[1], max_dp[2]) + b1
    new_max2 = max(max_dp[1], max_dp[2]) + b2
    max_dp = [new_max0, new_max1, new_max2]

    new_min0 = min(min_dp[0], min_dp[1]) + b0
    new_min1 = min(min_dp[0], min_dp[1], min_dp[2]) + b1
    new_min2 = min(min_dp[1], min_dp[2]) + b2
    min_dp = [new_min0, new_min1, new_min2]

print(max(max_dp), min(min_dp))
    

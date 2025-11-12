def solution(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]
    
    for i in range(1, n):
        # 가장 왼쪽
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        # 중간 부분
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - 1]) + triangle[i][j]
        # 가장 오른쪽
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        
    return max(dp[-1])
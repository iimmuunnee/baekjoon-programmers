def solution(m, n, puddles):
    MOD = 1_000_000_007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    # m : 열, n : 행
    # c : 열, r : 행
    
    for c, r in puddles:
        dp[r][c] = -1 # 물 웅덩이
        
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if dp[r][c] == -1:
                dp[r][c] = 0 # 물 웅덩이로는 올 수 없다
                continue
            if r == 1 and c == 1:
                continue
            dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % MOD
            
    return dp[n][m]
def solution(x, y, n):
    INF = float('inf')
    dp = [INF] * (y + 1)
    dp[x] = 0
    
    for i in range(x + 1, y + 1):
        cands = []
        if i % 3  == 0 and i // 3 >= x:
            cands.append(dp[i // 3])
        if i % 2 == 0 and i // 2 >= x:
            cands.append(dp[i // 2])
        if i - n  >= x:
            cands.append(dp[i - n])
        if cands:
            dp[i] = min(cands) + 1
        
    
    return dp[y] if dp[y] != INF else -1
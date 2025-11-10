def solution(n):
    answer = [[0 for _ in range(n)]for _ in range(n)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir = 0
    r, c = 0, 0
    
    for i in range(1, n**2 + 1):
        answer[r][c] = i
        nr = r + dirs[dir][0]
        nc = c + dirs[dir][1]
        
        if nr < 0 or nr >= n or nc < 0 or nc >= n or answer[nr][nc] != 0:
            dir = (dir + 1) % 4
            nr = r + dirs[dir][0]
            nc = c + dirs[dir][1]
        r = nr
        c = nc
        
    return answer
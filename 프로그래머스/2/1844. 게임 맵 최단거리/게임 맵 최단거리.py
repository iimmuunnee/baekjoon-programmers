from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1 # 출발지점
    
    q = deque()
    q.append((0, 0))
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        r, c = q.popleft() # 현재 위치
        if r == n - 1 and c == m - 1: # 도착지점이라면
            return dist[r][c]
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            # 1) 내부, 2) 벽이 아님 maps의 요소가 1, 3) 처음 오는 길 dist의 요소가 0
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
        
    return -1
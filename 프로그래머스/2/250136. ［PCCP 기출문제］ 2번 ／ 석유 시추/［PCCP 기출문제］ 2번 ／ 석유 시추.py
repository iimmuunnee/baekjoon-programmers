# DFS
from collections import deque

def bfs(start_x, start_y, group_num, land, visited, group, n, m):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    group[start_x][start_y] = group_num
    size = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    group[nx][ny] = group_num
                    queue.append((nx, ny))
                    size += 1
    return size

def solution(land):
    answer = 0
    n = len(land) # 세로
    m = len(land[0]) # 가로
    
    visited = [[False] * m for i in range(n)]
    group = [[-1] * m for i in range(n)]
    group_size = []
    
    group_num = 0
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = bfs(i, j, group_num, land, visited, group, n, m)
                group_size.append(size)
                group_num += 1
    
    
    
    for col in range(m):
        oil_set = set()
        
        for row in range(n):
            if land[row][col] == 1:
                oil_set.add(group[row][col])
        
        total_oil = 0
        for i in oil_set:
            total_oil += group_size[i]
        
        answer = max(answer, total_oil)
        
    
    return answer
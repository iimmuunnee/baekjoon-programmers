import sys
from collections import deque

# n은 세로, m은 가로

def bfs(target_map, m, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    visited = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if target_map[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if target_map[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    for i in range(n):
        for j in range(m):
            if target_map[i][j] == 0:
                sys.stdout.write("0 ")
            else:
                sys.stdout.write(str(visited[i][j]) + " ")
        sys.stdout.write("\n")

n, m = map(int, sys.stdin.readline().split())

target_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

bfs(target_map, m, n)
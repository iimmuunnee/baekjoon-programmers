import sys
from collections import deque
# 1은 이동 가능, 0은 이동 불가능 
# n X m 모양

def bfs(maze, n, m):
    # 인접한 곳으로만 이동 가능
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1: # 좌표가 범위 안에 있고 갈 수 있는 길인지 (1)
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]


n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

sys.stdout.write(str(bfs(maze, n, m)))
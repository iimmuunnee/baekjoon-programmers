import sys
from collections import deque

def bfs(town, visited, x, y, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    visited[x][y] = True # 방문함
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if town[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count



n = int(sys.stdin.readline())
town = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 1 and not visited[i][j]:
            cnt = bfs(town, visited, i, j, n)
            result.append(cnt)


sys.stdout.write(str(len(result)) + '\n')
for c in sorted(result):
    sys.stdout.write(str(c) + '\n')
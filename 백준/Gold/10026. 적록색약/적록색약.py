import sys
from collections import deque

def count_regions(is_color_weak):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited ,is_color_weak)
                count += 1
    return count

def bfs(x, y, visited, is_color_weak):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    current_color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()

        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                next_color = grid[nx][ny]
                if is_color_weak:
                    if (current_color in "RG" and next_color in "RG") or current_color == next_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if current_color == next_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

normal_count = count_regions(is_color_weak=False)
color_weak_count = count_regions(is_color_weak=True)

sys.stdout.write(str(normal_count) + " " + str(color_weak_count))
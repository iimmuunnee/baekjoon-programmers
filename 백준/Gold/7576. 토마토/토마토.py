import sys
from collections import deque

# m은 가로, n은 세로
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈 칸칸

def bfs(box, m, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0: # 범위 안에 있으면서 익지 않은 토마토일 때
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


m, n = map(int, sys.stdin.readline().split(" "))

box = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]

bfs(box, m, n)

day = 0

for row in box:
    for val in row:
        if val == 0:
            sys.stdout.write("-1")
            sys.exit()
        day = max(val, day)

sys.stdout.write(str(day - 1))
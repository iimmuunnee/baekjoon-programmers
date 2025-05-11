import sys
from collections import deque

# m은 가로, n은 세로
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈 칸칸

def bfs(box, m, n, h):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    queue = deque()

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 1:
                    queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h: # 범위 안에 있으면서 익지 않은 토마토일 때
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    queue.append((nx, ny, nz))


m, n, h = map(int, sys.stdin.readline().split(" "))
box = []

for _ in range(h):
    tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    box.append(tomato)

bfs(box, m, n, h)

day = 0

for layer in box:
    for row in layer:
        for val in row:
            if val == 0:
                sys.stdout.write("-1")
                sys.exit()
            day = max(val, day)

sys.stdout.write(str(day - 1))
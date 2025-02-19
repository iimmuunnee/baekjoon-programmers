import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

campus = [list(input().rstrip()) for _ in range(n)]

# I의 좌표 저장 및 캠퍼스 정보 저장
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            start_x, start_y = i, j
            break

queue = deque([(start_x, start_y)])
visited = [[False] * m for _ in range(n)]
visited[start_x][start_y] = True
count = 0 # 만난 사람 수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and visited[nx][ny] != "X":
            if campus[nx][ny] != "X":
                visited[nx][ny] = True
                queue.append((nx, ny))
                
                if campus[nx][ny] == "P":
                    count += 1

sys.stdout.write(f"{count if count > 0 else 'TT'}")

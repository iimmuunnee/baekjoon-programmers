import sys
from collections import deque
# 게임판 크기는 10x10 총 100칸. 주사위는 1~6, 

def bfs():
    queue = deque()
    queue.append((1, 0)) # (시작 칸, 주사위 횟수)
    visited = [False] * 101
    visited[1] = True

    while queue:
        cur, cnt = queue.popleft()

        if cur == 100:
            return cnt
        
        for dice in range(1, 7):
            next = cur + dice

            if next > 100:
                continue

            if next in ladder:
                next = ladder[next]
            elif next in snake:
                next = snake[next]

            if not visited[next]:
                visited[next] = True
                queue.append((next, cnt + 1))

# n: 사다리 개수, m: 뱀 개수
n, m = map(int, sys.stdin.readline().split()) 

ladder = dict()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ladder[x] = y


snake = dict()
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    snake[u] = v


sys.stdout.write(str(bfs()))
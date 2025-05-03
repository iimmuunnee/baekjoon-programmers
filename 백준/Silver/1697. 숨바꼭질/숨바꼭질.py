import sys
from collections import deque

def bfs(n, k):
    if n == k:
        return 0

    max_pos = 100001
    visited = [-1] * max_pos
    queue = deque([n])
    visited[n] = 0

    while queue:
        current = queue.popleft()

        for next in [current + 1, current - 1, current * 2]:
            if 0 <= next < max_pos and visited[next] == -1:
                visited[next] = visited[current] + 1
                queue.append(next)

                if next == k:
                    return visited[next]

n, k = map(int, sys.stdin.readline().split())

sys.stdout.write(str(bfs(n, k)))
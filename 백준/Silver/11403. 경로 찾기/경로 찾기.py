import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

def bfs(n, graph):
    result = [[0] * n for _ in range(n)]

    for start in range(n):
        visited = [0] * n
        queue = deque()
        queue.append(start)

        while queue:
            cur = queue.popleft()

            for next in range(n):
                if visited[next] == 0 and graph[cur][next] == 1:
                    visited[next] = 1
                    result[start][next] = 1
                    queue.append(next)

    return result


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

reach = bfs(n, graph)

for row in reach:
    print(" ".join(map(str, row)) + "\n")
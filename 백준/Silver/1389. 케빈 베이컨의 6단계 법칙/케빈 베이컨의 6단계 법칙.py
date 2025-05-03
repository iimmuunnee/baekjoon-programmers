import sys
from collections import deque

def bfs(start, graph, n):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return sum(visited[1:])

# n 유저의 수 1 ~ n
# m 친구 관계 수 = 줄의 수
n, m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)] # 각 유저가 어떤 유저랑 연결 되어 있는지

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

min_sum = float('inf')
answer = 0

for i in range(1, n + 1):
    total = bfs(i, graph, n)
    if total < min_sum:
        min_sum = total
        answer = i

print(answer)
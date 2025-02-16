import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

# DFS 구현
visited_dfs = [False] * (n + 1)

def dfs(v):
    visited_dfs[v] = True
    sys.stdout.write(f"{v} ")

    for next_v in graph[v]:
        if not visited_dfs[next_v]:
            dfs(next_v)

# BFS 구현
visited_bfs = [False] * (n + 1)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        current = queue.popleft()
        sys.stdout.write(f"{current} ")

        for next_v in graph[current]:
            if not visited_bfs[next_v]:
                queue.append(next_v)
                visited_bfs[next_v] = True

dfs(v)
sys.stdout.write("\n")
bfs(v)
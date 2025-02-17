import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n, m = map(int, input().rstrip().split())
graph = {i:[] for i in range(1, n+1)}
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a) # 무방향

# 연결요소 찾기
count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

sys.stdout.write(f"{count}")

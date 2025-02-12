import sys

input = sys.stdin.readline

n = int(input().strip()) # 컴퓨터 개수
k = int(input().strip()) # 컴퓨터 연결 쌍 개수

graph = {i:[] for i in range(1, n+1)}

for _ in range(k): # 연결된 노드 딕셔너리{[]}로 저장
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, visited): # dfs 탐색
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

visited = set()
dfs(1, visited)

sys.stdout.write(f"{len(visited) - 1}")
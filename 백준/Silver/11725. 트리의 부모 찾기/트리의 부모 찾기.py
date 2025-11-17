import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

links = [[] for _ in range(n+1)] # index 0 ~ 7인데 1 ~ 7만 사용

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    links[a].append(b)
    links[b].append(a)

parent = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(n):
    visited[n] = True
    for next in links[n]:
        if not visited[next]:
            parent[next] = n
            dfs(next)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])
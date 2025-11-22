import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int ,input().split())
MAX = 100000
# x -> x-1 (1초)
# x -> x+1 (1초)
# x -> 2*x (0초)

def bfs(n, k):
    dist = [float('inf')] * (MAX + 1)
    dist[n] = 0 # 수빈이의 시작점
    dq = deque([n])

    while dq:
        x = dq.popleft()

        if x == k:
            return dist[x]

        nx = x * 2
        if 0 <= nx <= MAX and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            dq.appendleft(nx)
        
        for nx in (x - 1, x + 1):
            if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
                dist[nx] = dist[x] + 1
                dq.append(nx)

    return dist[k]

print(bfs(n, k))
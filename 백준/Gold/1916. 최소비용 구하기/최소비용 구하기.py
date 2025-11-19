import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start, end):
    n = len(graph)
    heap = [(0, start)]
    d = [float('inf')] * (n + 1)
    d[start] = 0

    while heap:
        dist, curr = heapq.heappop(heap)
        if dist > d[curr]:
            continue  # 이미 더 좋은 경로로 갱신된 노드

        if curr == end:   # 끝까지 안 돌아도 됨 (옵션)
            break

        for child, w in graph[curr]:
            nd = dist + w # 다음까지의 가중치
            if nd < d[child]: # 다음까지의 가중치 < 기존에 있던 가중치
                d[child] = nd
                heapq.heappush(heap, (nd, child))

    return d[end]


n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

bus = {i : [] for i in range(1, n + 1)}

for i in range(m):
    s, e, w = map(int, input().split())
    bus[s].append((e, w))

a, b = map(int, input().split())

print(dijkstra(bus, a, b))
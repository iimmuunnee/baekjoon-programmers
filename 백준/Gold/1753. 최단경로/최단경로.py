import sys
import heapq

input = sys.stdin.readline
INF = float("inf")

def solution():
    V, E = map(int, input().split())
    K = int(input()) # 시작 정점

    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    distance = [INF] * (V + 1)

    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distance[start] = 0

        while queue:
            dist, current_node = heapq.heappop(queue)

            if distance[current_node] < dist:
                continue

            for next_node, weight in graph[current_node]:
                cost = dist + weight

                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))
    
    dijkstra(K)

    for i in range(1, V + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])


if __name__ == "__main__":
    solution()

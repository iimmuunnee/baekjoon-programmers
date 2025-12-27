import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def solution():
    N, E = map(int, input().split())


    # 양방향 그래프
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        # 양방향이라 양쪽에 추가
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    def dijkstra(start):
        # 시작점에서부터 각 정점까지의 거리를 기록
        distance = [INF] * (N + 1)
        distance[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))

        while queue:
            current_dist, current_node = heapq.heappop(queue)

            # 현재 경로가 더 길다면 스킵
            if distance[current_node] < current_dist:
                continue

            for neighbor, weight in graph[current_node]:
                cost = current_dist + weight

                if cost < distance[neighbor]:
                    distance[neighbor] = cost
                    heapq.heappush(queue, (cost, neighbor))
        
        return distance
    # 1로부터의 거리
    dist_from_1 = dijkstra(1)

    # 필수 정점 v1로부터의 거리
    dist_from_v1 = dijkstra(v1)

    # 필수 정점 v2로부터의 거리
    dist_from_v2 = dijkstra(v2)

    # 1 -> v1 -> v2 -> N
    path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

    # 1 -> v2 -> v1 -> N
    path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

    result = min(path1, path2)

    if result >= INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    solution()

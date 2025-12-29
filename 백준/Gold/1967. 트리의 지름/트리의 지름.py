import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    N = int(input()) # 노드의 개수

    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        parent, child, weight = map(int, input().split())
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))

    def dfs(node, current_dist):
        for next_node, weight in graph[node]:
            if distance[next_node] == -1:
                cost = current_dist + weight
                distance[next_node] = cost
                dfs(next_node, cost)

    # 1에서 가장 먼 노드를 찾고, 그 노드에서 가장 먼 노드까지의 거리를 찾아야 함
    distance = [-1] * (N + 1)
    distance[1] = 0
    dfs(1, 0)

    start_node = distance.index(max(distance))

    distance = [-1] * (N + 1)
    distance[start_node] = 0
    dfs(start_node, 0)

    print(max(distance))

if __name__ == "__main__":
    solution()

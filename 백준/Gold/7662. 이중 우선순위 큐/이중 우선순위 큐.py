import sys
import heapq

input = sys.stdin.readline
# print = sys.stdout.write

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = dict()
    cnt = 0

    for _ in range(k):
        op, n = input().split()
        n = int(n)

        if op == "I":
            heapq.heappush(min_heap, (n, cnt))
            heapq.heappush(max_heap, (-n, cnt))
            visited[cnt] = True
            cnt += 1

        elif op == "D":
            if n == 1: # 최대값 제거
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif n == -1:
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")
    else:
        print("EMPTY")
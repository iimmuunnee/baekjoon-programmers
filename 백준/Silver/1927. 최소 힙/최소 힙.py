import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            sys.stdout.write(f"{heapq.heappop(heap)}\n")
        else:
            sys.stdout.write("0\n")
    else:
        heapq.heappush(heap, num)
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

print = sys.stdout.write

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print("0\n")
        else:
            print(str(heapq.heappop(heap)[1]) + "\n")

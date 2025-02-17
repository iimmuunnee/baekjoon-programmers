import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 줄의 개수

heap = []

for _ in range(n):
    num = int(input()) # 입력받은 숫자

    if num == 0:
        if heap:
            sys.stdout.write(str(-heapq.heappop(heap)) + "\n")
        else:
            sys.stdout.write("0\n")
    else:
        heapq.heappush(heap, -num)

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque(range(1, n+1))
result = []

while deq:
    deq.rotate(-(k-1))
    result.append(deq.popleft())

print("<" + ", ".join(map(str, result)) + ">")
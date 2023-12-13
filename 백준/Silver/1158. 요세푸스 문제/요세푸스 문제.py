from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
arr = deque(list(range(1, n+1)))
result = []
while len(arr) > 0:
  for i in range(k - 1):
    arr.rotate(-1)
  result.append(str(arr.popleft()))

answer = ", ".join(result)
print("<" + answer + ">")
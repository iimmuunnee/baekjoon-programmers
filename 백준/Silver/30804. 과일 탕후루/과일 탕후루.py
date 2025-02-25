import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input()) # 과일의 개수
f = list(map(int, input().strip().split()))

window = deque()
fruit_count = defaultdict(int)
unique_fruits = 0 # 과일 종류수
max_length = 0

for right in range(n):
    window.append(f[right])
    fruit_count[f[right]] += 1

    if fruit_count[f[right]] == 1:
        unique_fruits += 1

    while unique_fruits > 2:
        removed = window.popleft()
        fruit_count[removed] -= 1
        if fruit_count[removed] == 0:
            unique_fruits -= 1

    max_length = max(max_length, len(window))

print(max_length)


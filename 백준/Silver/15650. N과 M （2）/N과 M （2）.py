import sys

input = sys.stdin.readline

n, m = map(int, input().split())
picked = []

def dfs(start: int):
    if len(picked) == m:
        print(*picked)
        return
    for num in range(start, n + 1):
        picked.append(num)
        dfs(num + 1)
        picked.pop()

dfs(1)
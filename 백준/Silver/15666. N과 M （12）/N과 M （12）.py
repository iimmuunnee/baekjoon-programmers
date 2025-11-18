import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i, depth + 1)
        path.pop()

dfs(0, 0)
            
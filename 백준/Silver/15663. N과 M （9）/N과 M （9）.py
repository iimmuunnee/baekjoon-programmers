import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False] * n
path = []

def dfs(depth):
    if depth == m:
        print(*path)
        return

    prev = None  # 이 depth에서 이미 쓴 값
    for i in range(n):
        if used[i]:
            continue
        if prev == nums[i]:   # 같은 깊이에서 같은 값은 한 번만
            continue

        used[i] = True
        path.append(nums[i])
        prev = nums[i]        # 이 depth에서 이 값은 썼다 표시

        dfs(depth + 1)

        path.pop()
        used[i] = False

dfs(0)

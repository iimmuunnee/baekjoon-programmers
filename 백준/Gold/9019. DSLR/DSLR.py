import sys
from collections import deque

def op(command, n):
    if command == 'D':
        return (n * 2) % 10000
    elif command == 'S':
        return 9999 if n == 0 else n - 1
    elif command == 'L':
        s = str(n).zfill(4)
        return int(s[1:] + s[0])
    elif command == 'R':
        s = str(n).zfill(4)
        return int(s[-1] + s[:-1])

def bfs(start, target):
    queue = deque()
    queue.append((start, []))
    visited = [False] * 10000
    visited[start] = True

    while queue:
        num, path = queue.popleft()

        if num == target:
            return ''.join(path)
        
        for command in ['D', 'S', 'L', 'R']:
            next_num = op(command, num)
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, path + [command]))

t = int(sys.stdin.readline()) # 테스트 케이스 개수
results = []
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    results.append(bfs(a, b))

print('\n'.join(results))
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if field[y][x] == 0:
        return
    
    field[y][x] = 0

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)


t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    m, n, k = map(int, input().rstrip().split()) # m: 가로, n: 세로, k: 배추의 좌표
    field = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        field[y][x] = 1 # 배추 심어진 위치

    worm_count = 0
    for i in range(m):
        for j in range(n):
            if field[j][i] == 1:
                dfs(i, j)
                worm_count += 1

    sys.stdout.write(f"{worm_count}\n")
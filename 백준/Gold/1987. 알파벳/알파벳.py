import sys

input = sys.stdin.readline

def solution():
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    # 이동 가능 방향 [x][y] 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = set([(0, 0, board[0][0])])

    answer = 1

    while queue:
        x, y, visited = queue.pop()

        answer = max(answer, len(visited))

        if answer == 26:
            print(26)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] not in visited:
                    queue.add((nx, ny, visited + board[nx][ny]))
        
    print(answer)

if __name__ == "__main__":
    solution()
    
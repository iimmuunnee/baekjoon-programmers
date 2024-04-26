def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 폭탄의 위치
    boom = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                boom.append((x, y))
    # 위험지역
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
                
    # 안전지대
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                cnt += 1
    
    return cnt
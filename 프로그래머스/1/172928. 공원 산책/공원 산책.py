def solution(park, routes):
    h, w = len(park), len(park[0])

    # 시작 지점 찾기
    for i, row in enumerate(park):
        for j, cell in enumerate(row):
            if cell == "S":
                y, x = i, j

    # 방향별 이동량 (dy, dx)
    move = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for route in routes:
        op, n = route.split()
        n = int(n)
        dy, dx = move[op]

        ny, nx = y, x
        ok = True
        for _ in range(n):          # 한 칸씩 가면서 확인
            ny += dy
            nx += dx
            if not (0 <= ny < h and 0 <= nx < w) or park[ny][nx] == "X":
                ok = False
                break

        if ok:                      # 끝까지 문제 없을 때만 실제로 이동
            y, x = ny, nx

    return [y, x]
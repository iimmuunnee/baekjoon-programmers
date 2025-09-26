from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(maze):
    n, m = len(maze), len(maze[0]) # n = 3, m = 2
    # 0 1 (n = 0) 
    # 2 3 (n = 1)
    # 4 5 (n = 2)
    
    def inside(x, y): # 좌표가 퍼즐판 위에 있는가?
        return 0 <= x < n and 0 <= y < m
    
    # 인덱스 <-> 좌표
    def idx(x, y):
        return x * m + y
    def xy(i):
        return divmod(i, m)
    
    
    R_start = B_start = R_goal = B_goal = -1
    walls = set()
    
    for i in range(n):
        for j in range(m):
            v = maze[i][j]
            if v == 1: 
                R_start = idx(i, j)
            elif v == 2:
                B_start = idx(i, j)
            elif v == 3:
                R_goal = idx(i, j)
            elif v == 4:
                B_goal = idx(i, j)
            elif v == 5:
                walls.add(idx(i, j))
                
    rv0 = 1 << R_start
    bv0 = 1 << B_start
    start = (R_start, B_start, rv0, bv0)
    
    # 수레가 현재 위치에서 움직일 수 있는 다음 위치들의 리스트 생성 함수
    def next_positions(pos, goal, visited_mask):
        x, y = xy(pos)
        if pos == goal: # 이미 목적지임
            return [pos]
        
        res = []
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if not inside(nx, ny):
                continue
            ni = idx(nx, ny)
            if ni in walls:
                continue
            if (visited_mask >> ni) & 1: # 방문한 칸이 이미 내가 방문했던 칸인지
                continue
            res.append(ni)
        return res
    
    #bfs
    q = deque()
    q.append((R_start, B_start, rv0, bv0, 0)) # (r, b, rv, bv, turns)
    seen = set([start])
    
    while q:
        r, b, rv, bv, t = q.popleft()
        if r == R_goal and b == B_goal: # 둘다 목적지에 도착
            return t
        
        r_next = next_positions(r, R_goal, rv)
        b_next = next_positions(b, B_goal, bv)
        
        for rn in r_next:
            for bn in b_next:
                # 같은 자리에 있기 방지
                if rn == bn:
                    continue
                # 자리바꾸기 금지
                if rn == b and bn == r:
                    continue
                    
                nrv = rv if rn == r else (rv | (1 << rn)) # rn번째칸만 1로 하고 그걸로 rv에 or연산으로 rn번째를 1로만듦
                nbv = bv if bn == b else (bv | (1 << bn))
                
                state = (rn, bn, nrv, nbv)
                if state in seen:
                    continue
                seen.add(state)
                q.append((rn, bn, nrv, nbv, t + 1))
    
    return 0
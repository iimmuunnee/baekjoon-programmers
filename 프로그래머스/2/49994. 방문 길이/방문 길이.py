def solution(dirs):
    answer = 0
    pos = (0, 0)
    edges = set()
    dx_dy_dict = {"U" : (0, 1), "D" : (0, -1), "R" : (1, 0), "L" : (-1, 0)}
    
    for c in dirs:
        dx, dy = dx_dy_dict[c]
        nx, ny = pos[0] + dx, pos[1] + dy
        if  -5 <= nx <= 5 and -5 <= ny <= 5:
            u = pos
            v = (nx, ny)
            edge = (u, v) if u < v else (v, u)
            edges.add(edge)
            pos = v
        
    answer = len(edges)
    
    return answer
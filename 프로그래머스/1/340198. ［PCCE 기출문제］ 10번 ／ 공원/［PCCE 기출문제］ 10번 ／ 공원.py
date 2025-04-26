def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    n = len(park)
    m = len(park[0])
    
    for size in mats:
        for i in range(n):
            for j in range(m):
                if i + size > n or j + size > m:
                    continue
                
                ok = True
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if park[x][y] != "-1":
                            ok = False
                            break
                    if not ok:
                        break
                
                if ok:
                    return size
    return -1
                            
        
            
    
    return answer
def solution(n, works):
    answer = 0
    if n >= sum(works):
        return 0
    s_works = sorted(works, reverse=True) + [0]
    n_left = n
    i = 0
    
    while n_left > 0 and i < len(s_works):
        gap = s_works[i] - s_works[i+1]
        need = gap * (i + 1)
        
        if n_left >= need:
            for j in range(i + 1):
                s_works[j] -= gap
            n_left -= need
            i += 1
        else:
            q, r = divmod(n_left, i+1)
            for j in range(i + 1):
                s_works[j] -= q
            for j in range(r):
                s_works[j] -= 1
            n_left = 0
            
    answer = sum(x*x for x in s_works[:-1] if x > 0)
    
    return answer
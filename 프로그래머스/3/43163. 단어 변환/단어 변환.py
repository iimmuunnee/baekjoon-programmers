from collections import deque

def adjacent(cur, w) -> bool:
    diff = 0
    for x, y in zip(cur, w):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer
    
    q = deque([(begin, 0)])
    visited = set([begin])
    while q:
        cur, d = q.popleft()
        if cur == target:
            return d
        for w in words:
            if w not in visited and adjacent(cur, w):
                visited.add(w)
                q.append((w, d+1))
        
    return answer
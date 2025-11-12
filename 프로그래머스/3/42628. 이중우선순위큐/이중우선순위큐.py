import heapq

def solution(operations):
    min_h, max_h = [], []
    alive = dict()
    uid = 0
    
    def gc(h):
        while h and not alive.get(h[0][1], False):
            heapq.heappop(h)
    
    for op in operations:
        if op[0] == 'I':
            x = int(op[2:])
            heapq.heappush(min_h, (x, uid))
            heapq.heappush(max_h, (-x, uid))
            alive[uid] = True
            uid += 1
        else:
            if op[2] == "1":
                gc(max_h)
                if max_h:
                    _, i = heapq.heappop(max_h)
                    alive[i] = False
            else:
                gc(min_h)
                if min_h:
                    _, i = heapq.heappop(min_h)
                    alive[i] = False
    gc(min_h); gc(max_h)
    if not min_h or not max_h:
        return [0,0]
        
    return [-max_h[0][0], min_h[0][0]]
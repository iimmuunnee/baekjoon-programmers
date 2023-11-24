from collections import deque
def solution(rc, operations):
    answer = []
    N = len(rc) # 행의 개수
    M = len(rc[0]) # 열의 개수
    center = deque(deque(row[1: -1]) for row in rc)
    first_c, last_c = deque(), deque()
    
    for i in range(N):
        first_c.append(rc[i][0]) # 각 행의 0번째 인덱스
        last_c.append(rc[i][-1]) # 각 행의 마지막 인덱스
    
    for oper in operations:
        if oper == "ShiftRow": # 마지막행 => 1행으로
            center.appendleft(center.pop()) # 가운데 마지막행을 가장 첫줄로 
            first_c.appendleft(first_c.pop())
            last_c.appendleft(last_c.pop())    
        elif oper == "Rotate":
            center[0].appendleft(first_c.popleft())
            last_c.appendleft(center[0].pop())
            center[-1].append(last_c.pop())
            first_c.append(center[-1].popleft())
            
    for i in range(N): # 떼어놓은 거 합치기
        cen = center[i]
        cen.appendleft(first_c[i])
        cen.append(last_c[i])
        answer.append(list(cen))
        
    return answer
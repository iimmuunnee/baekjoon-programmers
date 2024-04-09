def solution(priorities, location):
    # 큐 : FIFO
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]
    while True:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue): # 우선순위가 더 높은 게 있을 때
            queue.append(current)
        else: # 내가 우선순위 제일 높을 때
            answer += 1
            if current[0] == location:
                return answer
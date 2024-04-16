from collections import deque

def solution(numbers, direction):
    answer = []
    deq = deque(numbers)
    if direction == "right":
        deq.appendleft(deq.pop())
    else:
        deq.append(deq.popleft())
    return list(deq)
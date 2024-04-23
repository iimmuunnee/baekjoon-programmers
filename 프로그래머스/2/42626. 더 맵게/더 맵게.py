import heapq

def solution(scoville, k):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        answer += 1
    return answer
from collections import deque
def solution(queue1, queue2):
    # 리스트의 앞쪽이 먼저 집어넣은 원소
    # pop은 리스트의 첫번째 원소가 추출됨 리스트.insert(0 , 값)
    # insert는 리스트의 마지막 요소로 들어감 리스트.append(값)
    # 1. 두 큐에 담긴 모든 원소의 합을 구한다
    # 2. 2로 나눠서 각 큐의 합이 되어야 하는 값을 구한다.
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    all_sum = sum1 + sum2
    
    if all_sum % 2 != 0: # 합이 홀수일 때
        answer = -1
    else:
        for _ in range(len(queue1) * 4):
            if sum1 > sum2 :
                value = queue1.popleft()
                queue2.append(value)
                sum1 -= value
                sum2 += value
            elif sum1 < sum2 :
                value = queue2.popleft()
                queue1.append(value)
                sum1 += value
                sum2 -= value
            else:
                return answer
            answer += 1 
        
    return -1
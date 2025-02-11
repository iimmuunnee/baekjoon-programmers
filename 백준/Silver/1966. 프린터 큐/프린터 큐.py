import sys
from collections import deque

input = sys.stdin.readline

case = int(input()) # 테스트 케이스 개수

for _ in range(case):
    cnt = 1
    n, m = map(int, input().split())
    doc_list = list((map(int, input().split())))
    doc_que = deque((priority, index) for index, priority in enumerate(doc_list))
    # rotate 음수 => 왼쪽으로 이동
    while True:
        if max(doc_que)[0] > doc_que[0][0]: # 0번째 문서의 중요도가 가장 큰 중요도보다 작을 때 => rotate로 뒤로 넘기기
            doc_que.rotate(-1)
        else:
            if doc_que[0][1] == m:
                sys.stdout.write(f"{cnt}\n")
                break
            doc_que.popleft()
            cnt += 1
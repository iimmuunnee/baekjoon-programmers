import sys
import ast
from collections import deque

def AC(p, n, arr):
    reverse_flag = False # R이 홀수일 때 True, 짝수면 False 왜냐면 2번하면 다시 원래대로 오니까까

    for func in p:
        if func == "R":
            reverse_flag = not reverse_flag
            
        elif func == "D":
            if not arr:
                return "error"
            if reverse_flag:
                arr.pop()
            else:
                arr.popleft()
    if reverse_flag:
        arr.reverse()
    
    return "[" + ",".join(map(str, arr)) + "]"

t = int(sys.stdin.readline()) # 테스트 케이스 개수

for _ in range(t):
    p = sys.stdin.readline() # R과 D로 이루어진 함수 ex) RDD
    n = int(sys.stdin.readline()) # 배열의 요소 개수 = len(arr)
    arr = deque(ast.literal_eval(sys.stdin.readline())) # 배열9
    result = AC(p, n, arr)
    sys.stdout.write(result + "\n")
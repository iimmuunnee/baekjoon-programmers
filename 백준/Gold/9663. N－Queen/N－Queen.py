import sys

input = sys.stdin.readline

# 1. 같은 열에 있는가?
# 2. 오른쪽 위 대각선이 겹치는가?
# 3. 오른쪽 아래 대각선이 겹치는가?


def solution():
    n = int(input())

    # 1. 열(세로) 체크용 배열
    v1 = [False] * n
    
    # 2. 오른쪽 위 대각선(/) 체크용 배열 (x + y)
    # (0, 0) ~ (n-1, n-1) -> 2n - 2개인데 편의상 2n개
    v2 = [False] * (2 * n)
    
    # 3. 오른쪽 아래 대각선(\) 체크용 배열 (x - y)
    # 마찬가지
    v3 = [False] * (2 * n)
    
    count = 0

    # x는 현재 행 번호
    def dfs(x):
        nonlocal count
        
        if x == n:
            count += 1
            return
        # i는 현재 열 번호
        for i in range(n):
            # 세로(v1), 대각선1(v2), 대각선2(v3) 모두 False여야 놓을 수 있음
            if not v1[i] and not v2[x + i] and not v3[x - i + (n - 1)]:
                # 퀸을 놓는다 (True 체크)
                v1[i] = True
                v2[x + i] = True
                v3[x - i + (n - 1)] = True
                
                dfs(x + 1)
                
                # 백트래킹 (다시 False로 되돌림)
                v1[i] = False
                v2[x + i] = False
                v3[x - i + (n - 1)] = False

    dfs(0)
    print(count)

if __name__ == "__main__":
    solution()

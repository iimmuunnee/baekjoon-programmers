def solution(n):
    # 세로타일을 1, 가로 묶음 2개를 2
    a, b = 1, 2 
    if n == 1:
        return 1
    for _ in range(n - 2):
        a, b = b, (a + b) % 1_000_000_007

    
    return b
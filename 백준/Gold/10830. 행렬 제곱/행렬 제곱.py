import sys

input = sys.stdin.readline


def solution():
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    def mul_matrix(U, V):
        Z = [[0] * N for _ in range(N)] # 결과 행렬

        for row in range(N):
            for col in range(N):
                e = 0
                for k in range(N):
                    e += U[row][k] * V[k][col]
                    Z[row][col] = e % 1000
        return Z
    
    def square(a, b):
        if b == 1:
            for r in range(N):
                for c in range(N):
                    a[r][c] %= 1000
            return A
        
        temp = square(a, b // 2)
        if b % 2 == 0: # 짝수면
            return mul_matrix(temp, temp)
        else: # 홀수면 (짝수 + 1을 하면 원래 수인 홀수)
            return mul_matrix(mul_matrix(temp, temp), a)
    
    result = square(A, B)

    for row in result:
        print(*row)

if __name__ == "__main__":
    solution()

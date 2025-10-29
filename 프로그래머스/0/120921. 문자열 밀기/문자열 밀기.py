def solution(A, B):
    answer = -1
    n = len(A)
    i = 0
    while i < n:
        if A == B:
            answer = i
            break
        else:
            A = A[-1] + A[:-1]
            i += 1
    return answer
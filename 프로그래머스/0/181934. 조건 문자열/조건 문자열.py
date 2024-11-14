def solution(ineq, eq, n, m):
    answer = 0
    temp = True
    if ineq == ">" and eq == "=":
        temp = n >= m
    elif ineq == "<" and eq == "=":
        temp = n <= m
    elif ineq == ">" and eq == "!":
        temp = n > m
    elif ineq == "<" and eq == "!":
        temp = n < m
        
    if temp:
        answer = 1
        
    return answer
def solution(a, b, c):
    answer = 0
    
    result = set()
    result.update([a, b, c])
    n = len(result)
    
    if n == 3:
        answer = a + b + c
    elif n == 2:
        answer = (a + b + c) * (a**2 + b**2 + c**2) 
    elif n == 1:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

    return answer
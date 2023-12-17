from math import gcd

def solution(arr):
    answer = 1 # 최소공배수
    
    for i in arr:
        answer = answer * i // gcd(answer, i)
    
    return answer
import math

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        
def is_primenum(x):
    for i in range (2, int(math.sqrt(x)) + 1):
    	if x % i == 0:
        	return False
    return True
        
def solution(a, b):
    answer = 1
    gd = gcd(a, b)
    b = b // gd
    for i in range(2, b + 1):
        if b % i == 0 and is_primenum(i):
            if i not in [2, 5]:
                return 2
    return answer


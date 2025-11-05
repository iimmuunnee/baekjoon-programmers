from functools import cmp_to_key

def solution(numbers):
    strs = list(map(str, numbers))
    
    def cmp(a, b):
        if a + b > b + a: return -1
        if a + b < b + a: return 1
        return 0
    
    strs.sort(key=cmp_to_key(cmp))
    
    if strs[0] == '0':
        return '0'
    else:
        return "".join(strs)
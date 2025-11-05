from itertools import combinations
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n_list = list(combinations(nums, 3))
    
    for combi in n_list:
        if is_prime(sum(combi)):
            answer += 1
    
    return answer
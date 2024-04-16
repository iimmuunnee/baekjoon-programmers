def solution(numbers, k):
    answer = 0
    n = len(numbers)
    # 0 2 4 6 8
    n = len(numbers)
    num1 = 2 * (k - 1) # 인덱스
    num2 = (num1 % n) 
    answer = numbers[num2]
    
    return answer
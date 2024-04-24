import re
def solution(my_string):
    answer = 0
    pattern = r'[^0-9]+' # 정규표현식 패턴 숫자가 아닌거 날때마다 
    result = re.split(pattern, my_string)
    result = [int(num) for num in result if num]
    answer = sum(result)
    
    return answer
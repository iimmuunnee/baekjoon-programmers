import re

def solution(myStr):
    answer = []
    result = re.split('a|b|c', myStr)
    answer = [item for item in result if item != '']
    if answer == []:
        answer = ['EMPTY']
    return answer
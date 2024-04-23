import re

def solution(numbers):
    number_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    pattern = re.compile('|'.join(number_dict.keys()))
    result = pattern.sub(lambda x: number_dict[x.group()], numbers)
    answer = int(result)
    return answer

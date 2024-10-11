def solution(myString):
    answer = ''
    table = str.maketrans('abcdefghijk', 'lllllllllll')
    answer = myString.translate(table)
    return answer
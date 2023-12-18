from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    s = list(s) # 암호 문자열 리스트
    skip = list(skip) # 스킵할 문자열 리스트
    alpha_list = list(ascii_lowercase) # 전체 알파벳

    alpha_list = list(set(alpha_list) - set(skip)) # 스킵하는 문자 제외하기
    n = len(alpha_list) # 사용가능한 전체 알파벳 개수
    alpha_list.sort() # 알파벳 정렬
    for i in s:
        alpha_index = alpha_list.index(i)
        answer += alpha_list[(alpha_index + index) % n]
    return answer
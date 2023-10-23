def solution(clothes):
    answer = 1
    category = {} # 옷의 종류를 key로하고 개수를 value로하는 딕셔너리 생성
    # 종류와 개수 딕셔너리에 넣기
    for item in clothes:
        category[item[1]] = category.get(item[1], 0) + 1
    
    for key, value in category.items():
        answer *= value + 1
    
    return answer - 1
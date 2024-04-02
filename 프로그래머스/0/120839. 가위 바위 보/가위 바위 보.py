def solution(rsp):
    answer = ''
    # 2는 0으로
    # 0은 5로
    # 5는 2로
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"
    return answer
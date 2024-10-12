def solution(myString):
    answer = []
    count = 0
    for word in myString:
        if word != "x":
            count += 1
        else:
            answer.append(count)
            count = 0
    answer.append(count)
    return answer
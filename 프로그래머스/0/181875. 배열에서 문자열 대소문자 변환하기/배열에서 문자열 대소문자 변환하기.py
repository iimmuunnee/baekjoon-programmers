def solution(strArr):
    answer = []
    for i in range(0, len(strArr), 2):
        strArr[i] = strArr[i].lower()
    for j in range(1, len(strArr), 2):
        strArr[j] = strArr[j].upper()
    return strArr
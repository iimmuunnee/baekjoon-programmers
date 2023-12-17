def solution(elements):
    answer = 0
    n = len(elements)
    elements = elements + elements
    arr = []
    for i in range(n+1): # 1 ~ 5 길이
        if i < n + 1:
            for j in range(n): # 0 ~ 4 인덱스 시작
                arr.append(sum(elements[j:j+i % n]))
        elif i == n + 1:
            arr.append(sum(elements))
    arr = list(set(arr))
    return len(arr)
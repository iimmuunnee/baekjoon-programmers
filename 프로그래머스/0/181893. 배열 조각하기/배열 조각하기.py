def solution(arr, query):
    answer = []
    # 인덱스가 짝수면 앞부분만, 홀수면 뒷부분만
    for i, v in enumerate(query):
        if i % 2 == 0:
            arr = arr[:v+1]
        else:
            arr = arr[v:]
    return arr
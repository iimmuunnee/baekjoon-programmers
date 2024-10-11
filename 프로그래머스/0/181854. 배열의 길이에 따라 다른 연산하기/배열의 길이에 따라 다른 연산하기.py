def solution(arr, n):
    answer = []
    len_arr = len(arr)
    if len_arr % 2 == 0: # 짝수 길이, 홀수 인덱스 위치에 n 더하기
        for i in range(1, len_arr, 2):
            arr[i] += n
    else:
        for j in range(0, len_arr, 2):
            arr[j] += n
    return arr
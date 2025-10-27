def solution(arr):
    if 2 not in arr:
        return [-1]
    answer = []
    index_list = [i for i, v in enumerate(arr) if v == 2]
    answer = arr[index_list[0] : index_list[-1] + 1]
    return answer
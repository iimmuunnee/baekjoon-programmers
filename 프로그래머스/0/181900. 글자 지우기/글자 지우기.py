def solution(my_string, indices):
    answer = ''
    arr = [s for s in my_string]
    for i in indices:
        arr[i] = ""
    for i in arr:
        answer += i
    return answer
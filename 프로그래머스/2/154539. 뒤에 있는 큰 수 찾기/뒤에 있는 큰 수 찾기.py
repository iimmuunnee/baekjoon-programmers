def solution(numbers):
    answer = [-1] * len(numbers)
    index = []
    for i in range(len(numbers)):
        num = numbers[i]
        while index and numbers[index[-1]] < num:
            answer[index.pop()] = num
        index.append(i)
    return answer
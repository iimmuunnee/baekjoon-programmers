def solution(numbers, num1, num2):
    answer = []
    number = numbers[num1 : num2 + 1]
    answer.extend(number)
    return answer
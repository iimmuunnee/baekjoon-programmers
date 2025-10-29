def solution(my_string):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = [0] * 52
    for c in my_string:
        if c in alpha:
            i = alpha.find(c)
            answer[i] += 1
    return answer
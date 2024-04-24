def solution(before, after):
    answer = 1
    unique_chars = list(set(before))
    for char in unique_chars:
        if before.count(char) != after.count(char):
            answer = 0
            break
    return answer
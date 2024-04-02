def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
def solution(n):
    answer = 0
    piece = lcm(6, n)
    answer = piece / 6
    return answer
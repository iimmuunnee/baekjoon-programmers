def solution(numlist, n):
    answer = []
    numlist_2 = list(map(lambda x: (x, abs(x - n)), numlist))
    numlist_2.sort(key=lambda x: (x[1], -x[0]))
    answer = list(map(lambda x: x[0], numlist_2))
    return answer
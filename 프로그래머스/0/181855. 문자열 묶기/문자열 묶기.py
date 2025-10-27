from collections import defaultdict

def solution(strArr):
    answer = 0
    len_dict = defaultdict(int)
    for w in strArr:
        n = len(w)
        len_dict[n] += 1
    answer = max(len_dict.values())
    return answer 
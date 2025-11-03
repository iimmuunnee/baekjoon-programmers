import numpy as np

def solution(n, m, section):
    answer = 0
    np_section = np.array(section)
    num = 1
    while len(np_section) != 0:
        mask = np_section >= np_section[0] + m * num
        np_section = np_section[mask]
        n += 1
        answer += 1
    return answer
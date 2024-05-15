def solution(lines):
    answer = 0
    sets = [set(range(l[0], l[1])) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
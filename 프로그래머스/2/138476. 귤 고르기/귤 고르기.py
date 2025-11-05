import collections

def solution(k, tangerine):
    cnt_counter = collections.Counter(tangerine)
    
    s, kinds = 0, 0
    for _, f in cnt_counter.most_common():
        s += f
        kinds += 1
        if s >= k:
            return kinds
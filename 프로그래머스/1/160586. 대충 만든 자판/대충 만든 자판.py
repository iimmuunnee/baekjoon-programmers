def build_min_pos(keymap):
    best = {}
    for key in keymap:
        for i, ch in enumerate(key, start=1):
            if ch not in best or i < best[ch]:
                best[ch] = i
    return best

def min_strokes(word, best):
    s = 0
    for ch in word:
        v = best.get(ch)
        if v is None:
            return -1
        s += v
    return s

def solution(keymap, targets):
    answer = []
    best = build_min_pos(keymap)
    for word in targets:
        s = min_strokes(word, best)
        answer.append(s)
        
    return answer
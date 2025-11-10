def solution(word):
    pos = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    W = [781, 156, 31, 6, 1]
    ans = 0
    for i, ch in enumerate(word):
        ans += pos[ch] * W[i] + 1
    return ans

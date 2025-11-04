from collections import Counter

def make_bigrams(s):
    s = s.upper()
    bags = []
    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        if a.isalpha() and b.isalpha():        # 두 글자 모두 알파벳일 때만
            bags.append(a + b)
    return Counter(bags)                       # 다중집합

def solution(str1, str2):
    c1 = make_bigrams(str1)
    c2 = make_bigrams(str2)

    # 둘 다 공집합이면 유사도 1 → 65536
    if not c1 and not c2:
        return 65536

    inter = sum((c1 & c2).values())            
    union = sum((c1 | c2).values())           
    return int(inter / union * 65536)

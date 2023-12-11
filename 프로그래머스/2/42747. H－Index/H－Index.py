def solution(citations):
    answer = 0
    len_cit = len(citations)
    max_cit = max(citations)
    inyong = 0 # h번 인용된 논문 -> j
    h = 0 # h번 이상 -> i
    
    for i in range(max_cit + 1): # 0 ~ 5 / i 번 이상 인용된
        for j in citations:
            if i < j:
                h += 1
        if h == i:
            answer = h
            break
        else:
            answer = 0
            h = 0
        
    return answer
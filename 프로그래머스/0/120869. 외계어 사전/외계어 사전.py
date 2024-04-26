def solution(spell, dic):
    answer = 2
    for d in dic:
        cnt = 0
        for s in spell:
            if d.count(s) == 1:
                cnt += 1
                if cnt == len(spell):
                    return 1
        
    return answer
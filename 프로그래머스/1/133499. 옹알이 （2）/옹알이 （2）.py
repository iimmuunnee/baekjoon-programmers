def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        before = None
        buf = ""
        ok = True
        
        for c in s:
            buf += c
            
            if not any(w.startswith(buf) for w in can):
                ok = False
                break
            
            if buf in can:
                if buf == before:
                    ok = False
                    break
                before = buf
                buf = ""
        if buf == "" and ok:
            answer += 1
            
    return answer
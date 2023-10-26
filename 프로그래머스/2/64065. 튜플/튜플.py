def solution(s):
    answer = []
    s = s[2 : -2]
    s = s.replace("},{", "@")
    s = s.split("@")
    s2 = []
    for idx, item in enumerate(s):
        s2 = item.split(",")
        s[idx] = s2
    sorted_s = sorted(s, key=lambda x : len(x))
    for i in sorted_s:
        for j in i:
            j = int(j)
            if j not in answer:
                answer.append(j)
                break
            else:
                continue
    
    return answer
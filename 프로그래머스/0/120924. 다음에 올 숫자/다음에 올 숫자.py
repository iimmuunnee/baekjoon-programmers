def solution(common):
    answer = 0
    diff = 0
    how = ""
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        how = "diff"
    elif common[1] / common[0] == common[2] / common[1]:
        diff = common[1] / common[0]
        how = "multi"
    
    print(f"diff = {diff}")
    if how == "diff":
        answer = common[-1] + diff
    else:
        answer = common[-1] * diff
    
    return answer
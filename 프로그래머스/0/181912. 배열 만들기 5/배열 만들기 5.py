def solution(intStrs, k, s, l):
    answer = []
    
    for intstr in intStrs:
        answer.append(int(intstr[s:s+l]))
    
    return [i for i in answer if i > k]
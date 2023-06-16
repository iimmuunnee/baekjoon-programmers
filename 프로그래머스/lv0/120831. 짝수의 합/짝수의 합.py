def solution(n):
    answer = 0
    alist=[]
    nlist = list(range(n+1))
    for x in nlist:
        if x % 2 ==0:
            alist.append(x)
    answer = sum(alist)
    return answer
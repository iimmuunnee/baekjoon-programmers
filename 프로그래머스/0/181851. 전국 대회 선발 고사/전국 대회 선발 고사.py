def solution(rank, attendance):
    idx_list = [i for i, att in enumerate(attendance) if att]
    idx_list.sort(key=lambda i: rank[i])
    a, b, c = idx_list[:3]
    
    return 10000 * a + 100 * b + c
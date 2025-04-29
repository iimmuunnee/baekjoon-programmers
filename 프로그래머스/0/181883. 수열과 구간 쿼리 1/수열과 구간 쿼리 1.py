def solution(arr, queries):
    n = len(arr)
    diff = [0] * (n + 1) # 누적합 리스트 n + 1인 이유는 마지막 인덱스에서 누적합을 멈추기 위해 -1을 넣을 때 인덱스 오류 방지
    
    for s, e in queries:
        diff[s] += 1
        diff[e + 1] -= 1 # 누적 합 할때 -1로 +1을 0으로 상쇄시켜서 범위 그 다음 누적합에 영향을 안 줌
        
    for i in range(1, n):
        diff[i] += diff[i - 1]

    return [arr[i] + diff[i] for i in range(n)]
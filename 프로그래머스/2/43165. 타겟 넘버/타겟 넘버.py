def solution(numbers, target):
    leaves = [0] # 모든 계산 결과를 담을 리스트
    answer = 0
    
    for num in numbers:
        temp = [] # 계산 결과를 임시로 담을 리스트
        
        # 자식노드
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        leaves = temp
    
    for leaf in leaves:
        if leaf == target:
            answer += 1
    
    return answer
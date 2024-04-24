def solution(sides):
    answer = 0
    max_sides = max(sides)
    # 주어진 변중 가장 긴 변이 가장 긴 변일때
    for i in range(1, max_sides):
        if max_sides < min(sides) + i:
            answer += 1
    # 새로 주어지는 변이 가장 긴 변일때
    for j in range(max_sides, sum(sides)):
        answer += 1
    
    return answer
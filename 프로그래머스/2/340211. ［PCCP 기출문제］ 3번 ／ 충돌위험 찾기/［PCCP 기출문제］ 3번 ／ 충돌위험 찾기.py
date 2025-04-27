from collections import defaultdict, Counter

def solution(points, routes):
    answer = 0
    point_map = {}
    
    for idx, (r, c) in enumerate(points):
        point_map[idx + 1] = (r, c)
    
    time_positions = defaultdict(list)
    
    # 로봇 하나의 경로
    for robot_route in routes:
        time = 0
        
        # 출발지
        start_point = robot_route[0] # ex) start_point = 4
        r, c = point_map[start_point] # ex) r, c = 1, 4
        
        time_positions[time].append((r, c))
        
        # 목적지
        for target_point in robot_route[1:]:
            target_r, target_c = point_map[target_point]
            
            # r 먼저
            while (r != target_r):
                if (r < target_r):
                    r += 1
                elif (r > target_r):
                    r -= 1
                
                time += 1
                time_positions[time].append((r, c))
                
            # c 이동
            while c != target_c:
                if c < target_c:
                    c += 1
                elif c > target_c:
                    c -= 1
                time += 1
                time_positions[time].append((r, c))
    
    for time in time_positions:
        counter = Counter(time_positions[time])
        
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1

    return answer
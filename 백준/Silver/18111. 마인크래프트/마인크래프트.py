import sys
from collections import Counter

input = sys.stdin.readline
# 가능한 블럭 높이 0~256, h = 2 x 제거블록 + 추가 블록 개수 
n, m, b = map(int, input().rstrip().split()) # n: 세로, m: 가로, b: 인벤토리에 있는 블럭

ground = []
for _ in range(n):
    ground.extend(map(int, input().rstrip().split()))

height_counts = Counter(ground)

min_h = min(height_counts)
max_h = max(height_counts)

min_time = float('inf')
optimal_h = 0

for h in range(min_h, max_h + 1): # h: 목표 높이
    remove_b = 0 # 제거한 블록
    add_b = 0 # 추가한 블록

    for height, count in height_counts.items():
        diff = height - h

        if diff > 0: # 제거해야됨
            remove_b += diff * count
        elif diff < 0: # 추가해야됨
            add_b -= diff * count
            
    if remove_b + b >= add_b: # 인벤토리에 블록이 추가할만큼 충분히 있는지
        time = (remove_b * 2) + add_b
        
        if time < min_time:
            min_time = time
            optimal_h = h
        elif time == min_time and h > optimal_h:
            optimal_h = h

sys.stdout.write(f"{min_time} {optimal_h}")
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = [] # 집의 좌표
chickens = [] # 치킨집 좌표

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

min_city_chicken_distance = float('inf')

for selected_chickens in combinations(chickens, M):
    total = 0 # 현재 선택된 치킨집의 도시 치킨거리

    for hr, hc in house:
        min_dist = float('inf') # 집에서 가장 가까운 치킨거리

        for cr, cc in selected_chickens:
            dist = abs(hr - cr) + abs(hc - cc)
            min_dist = min(min_dist, dist)

        total += min_dist

        if total >= min_city_chicken_distance: # 넘으면 필요없음
            break

    if total < min_city_chicken_distance: # 최소 도시 치킨 거리 최신화
        min_city_chicken_distance = total

print(min_city_chicken_distance)
        
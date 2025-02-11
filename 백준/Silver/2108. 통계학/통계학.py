import sys
from collections import Counter

input = sys.stdin.readline

# 산술평균 함수
def arithmetic_mean(num_list): 
    return round(sum(num_list) / len(num_list))

# 중앙값 함수
def median(num_list):
    num_list.sort()
    return num_list[len(num_list) // 2]

# 최빈값 함수
def mode(num_list):
    counter = Counter(num_list)
    max_count = counter.most_common(1)[0][1] # 가장 많이 나온 횟수
    most_frequent = [num for num, count in counter.items() if count == max_count]
    most_frequent.sort()
    if len(most_frequent) > 1:
        return most_frequent[1]
    return most_frequent[0]

# 범위 함수수
def num_range(num_list):
    return max(num_list) - min(num_list)

n = int(input()) # n은 홀수, 숫자의 개수

num_list = [int(input()) for _ in range(n)]

results = [
    str(arithmetic_mean(num_list)),
    str(median(num_list)),
    str(mode(num_list)),
    str(num_range(num_list))
]

sys.stdout.write("\n".join(results))
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

num_list = list(map(int, input().rstrip().split()))

# 누적합
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num_list[i - 1] # num_list는 인덱스 0이 1번째니까

# 구간 합
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    result = prefix_sum[b] - prefix_sum[a - 1] # 인덱스와 n번째의 차이
    sys.stdout.write(f"{result}\n")
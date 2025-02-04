import sys

n, m = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
temp = []
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum_num = num_list[i] + num_list[j] + num_list[k]
      if m >= sum_num:
        temp.append(sum_num)
      else:
        continue

sys.stdout.write(str(max(temp)))
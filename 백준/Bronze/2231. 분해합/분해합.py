import sys

n = int(sys.stdin.readline()) # 자연수 n

for i in range(1, n+1):
  num_list = list(map(int, str(i)))
  temp = sum(num_list) + i
  if temp == n:
    sys.stdout.write(str(i))
    break
  if i == n:
    sys.stdout.write("0")
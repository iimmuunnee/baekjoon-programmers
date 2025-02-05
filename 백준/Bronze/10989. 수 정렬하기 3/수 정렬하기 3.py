import sys

n = int(sys.stdin.readline().rstrip())
cnt_dic = {}

for i in range(n):
  num = int(sys.stdin.readline().rstrip())
  if num in cnt_dic:
    cnt_dic[num] += 1
  else:
    cnt_dic[num] = 1 

for i in range(max(cnt_dic.keys()) + 1):
  if i in cnt_dic:
    for _ in range(cnt_dic[i]):
      sys.stdout.write((str(i) + "\n"))
  else:
    continue
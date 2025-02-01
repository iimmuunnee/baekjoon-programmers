import sys

max = 1000000 # 최댓값 설정

M = [0 for i in range(max+1)] # 누적합
m = [0 for i in range(max+1)] # 약수합

for i in range(1, max+1):
  j = 1
  while i*j <= max:
    m[i*j] += i
    j += 1
  M[i] = M[i-1] + m[i]

n = int(input())
div_list = list()
for i in range(n):
  num = int(sys.stdin.readline())
  div_list.append(num)

for i in div_list:
  sys.stdout.write(str(M[i])+"\n")
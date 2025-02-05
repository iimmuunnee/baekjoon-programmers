import sys

t = int(sys.stdin.readline()) # 테스트 케이스 수

for i in range(t): 
  k = int(sys.stdin.readline()) # k층
  n = int(sys.stdin.readline()) # n호

  apt = [[0] * (n + 1) for i in range(k+1)]

  for i in range(1, n+1): # 0층은 i호에 i명
    apt[0][i] = i
  
  for floor in range(1, k+1):
    for room in range(1, n+1):
      apt[floor][room] = apt[floor][room - 1] + apt[floor - 1][room]

  sys.stdout.write(str(apt[k][n]) + "\n")
    

# 3층 1 5 15 35
# 2층 1 4 10 20 35
# 1층 1 3 6 10 15
# 0층 1 2 3 4 5 
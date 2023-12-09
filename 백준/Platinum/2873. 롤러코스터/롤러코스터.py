import sys
r, c = map(int, sys.stdin.readline().split()) # 행, 열
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
route = ''
if r % 2 == 1: # 행이 홀수
  print(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1: # 열이 홀수
  print(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))
elif (r % 2 == 0 and c % 2 == 0):
  min = 1000 # 최솟값
  min_x = -1
  min_y = -1
  # 최소값 위치 찾기
  for i in range(r):
    for j in range(c):
      # 짝수행에 대하여 
      if((i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0)):
        if(min > arr[i][j]):
          min = arr[i][j]
          min_x = i
          min_y = j
  # 1. 빈 칸 이전 열에 대한 경로(DRUR)
  route += ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (min_y // 2)
  #route += " "    

  # 2. 빈 칸을 둘러싼 경로
  y1 = (min_y // 2) * 2      # 첫번째 열
  y2 = (min_y // 2) * 2 + 1  # 두번째 열
  x = 0    # 2번 경로 시작 행
  y = y1   # 2번 경로 시작 열

  while True:
    # 마지막 행, 두번째 열이면 탈출
    if(x == r - 1 and y == y2):
      break
    # 1-1.현재 첫번째 열이고 오른쪽 칸이 빈칸이 아니면 오른쪽으로
    if(y == y1 and [x, y2] != [min_x, min_y]):
      route += 'R'
      y += 1
    # 1-2. 현재 두번째 열이고 왼쪽 칸이 빈칸이 아니면 왼쪽으로
    elif(y == y2 and [x, y1] != [min_x, min_y]):
      route += 'L'
      y -= 1
    # 2. 마지막 행이 아니면 아래로
    if(x != r - 1):
      route += 'D'
      x += 1
  #route += " "   

  # 3. 빈 칸 이후 열에 대한 경로(RURD)
  route += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - min_y - 1) // 2)

print(route)
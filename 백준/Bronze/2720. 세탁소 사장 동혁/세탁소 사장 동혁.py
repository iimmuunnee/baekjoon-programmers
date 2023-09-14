array = [0 for i in range(4)]

n = int(input())  # 입력 받는 횟수

for i in range(n):
  k = int(input())
  array[0] = k // 25
  array[1] = k % 25 // 10
  array[2] = k % 25 % 10 // 5
  array[3] = k % 25 % 10 % 5 // 1
  print(*array)
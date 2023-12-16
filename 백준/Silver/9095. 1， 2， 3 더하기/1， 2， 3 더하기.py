n = int(input())  # 테스트 개수

for number in range(n):
  test = int(input())
  arr = [0] * (test + 1)
  for i in range(1, test + 1):
    if i == 1:
      arr[i] = 1
    elif i == 2:
      arr[i] = 2
    elif i == 3:
      arr[i] = 4
    else:
      arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
  print(arr[i])
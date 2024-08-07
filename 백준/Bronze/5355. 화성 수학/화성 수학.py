import math

n = int(input())
for i in range(n):
  arr = input().split(" ")
  arr[0] = float(arr[0])
  arr[0] = math.floor(arr[0] * 100) / 100
  number = arr[0]
  arr = arr[1:]
  for j in arr:
    if j == "@":
      number *= 3.00
    elif j == "%":
      number += 5.00
    elif j == "#":
      number -= 7.00
  print(f"{number:.2f}")

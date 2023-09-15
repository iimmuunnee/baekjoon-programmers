n = int(input())
x_array = []
y_array = []

for _ in range(n):
  x, y = map(int, input().split())
  x_array.append(x)
  y_array.append(y)

max_x = max(x_array)
min_x = min(x_array)
max_y = max(y_array)
min_y = min(y_array)

if(max_x == min_x or max_y == min_y):
  print(0)
else:
  print((max_x - min_x) * (max_y - min_y))
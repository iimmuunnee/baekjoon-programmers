x_array = []
y_array = []
result_x = 0
result_y = 0

for _ in range(3):
  x, y = map(int, input().split())
  x_array.append(x)
  y_array.append(y)

x_set_list = list(set(x_array))
y_set_list = list(set(y_array))

for x in x_set_list:
  if(x_array.count(x) == 1):
    result_x = x

for y in y_set_list:
  if(y_array.count(y) == 1):
    result_y = y

print(result_x, result_y)
n = int(input()) # 목표 채널
error_num = int(input())
result = abs(100 - n)
if error_num:
    err_arr = set(input().split())
else:
    err_arr = set()

for i in range(1000001):
  for num in str(i):
    if num in err_arr:
      break
  else:
    result = min(result, len(str(i)) + abs(i - n))

print(result)
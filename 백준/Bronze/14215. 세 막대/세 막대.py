a, b, c = map(int, input().split())

array = [a, b, c]
max_k = max(array)
array.remove(max_k)

if(sum(array) > max_k):
  print(sum(array) + max_k)
else:
  mak_k = sum(array) - 1
  result = mak_k + sum(array)
  print(result)
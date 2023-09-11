n, m = map(int, input().split())
answer = ''

array = [0 for i in range(n)]

for _ in range(m):
  i, j, k = map(int, input().split())
  for n in range(i, j+1):
    array[n-1] = k
    
for i in array:
  print(i, end=" ")
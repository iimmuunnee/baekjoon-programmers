n, m = map(int, input().split())

# 바구니 번호 : 1 ~ n
# 바구니 인덱스 : 0 ~ n-1 

array = [i for i in range(1, n+1)] 

for _ in range(m):
  i, j = map(int, input().split())
  array[i - 1], array[j - 1] = array[j - 1], array[i - 1]
  
for i in array:
  print(i, end=" ")
result = 0 # 동전 개수
index = 0
n, k = map(int, input().split())
A_arr = []
for i in range(n):
  A_arr.append(int(input()))
  
for i in range(n):
  if k > 0:
    if k < A_arr[i]:
      result += k // A_arr[i-1] # 몫이 동전 갯수
      index = i - 1
      k = k % A_arr[i-1] # 나머지가 곧 k가 된다
      break

while k > 0:
  index -= 1
  result += k // A_arr[index]
  k = k % A_arr[index] # 나머지가 곧 k가 된다
  
print(result)
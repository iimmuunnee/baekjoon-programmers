from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 1
end = max(arr)

while (start <= end):
    sum = 0
    mid = (start + end) // 2 # 자르는 기준 처음은 중간
    for i in arr:
        if i > mid:
          sum += i - mid
    if sum < m: # 덜 잘렸을 때 높이를 낮추기
      end = mid - 1
    else:
      start = mid + 1
      
print(end)
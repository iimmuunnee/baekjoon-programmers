result = 0 # 정답
n = int(input()) # 인원 수
p_array = list(map(int, input().split()))
p_array.sort()

for i in range(n):
  result += sum(p_array[:i+1])
print(result)
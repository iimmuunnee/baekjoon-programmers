
n = input()
if '0' not in n:
  print(-1)
else:
  num_sum = 0 # 3의 배수는 모두 더했을 때 3의 배수여야 한다.
  for i in range(len(n)):
    num_sum += int(n[i])

  if num_sum % 3 != 0:
    print(-1)
  else:
    sorted_num = sorted(n, reverse=True)
    answer = "".join(sorted_num)
    print(answer)
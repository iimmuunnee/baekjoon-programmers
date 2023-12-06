result = 0 # 첫번째 숫자
minus_result = 0 # 그 이후 숫자들을 모두 빼기 기준으로 나누고 다 더한후 첫번째 숫자에서 빼주기만 하면 됨
str = input()
number_arr = str.split('-')
for index, i in enumerate(number_arr):
  if index == 0:
    if '+' in i:
      result = sum(map(lambda x: int(x.lstrip('0')), i.split('+'))) # 0으로 시작하는 숫자 검증
    else:
      result = int(i)
  else:
    if '+' in i:
      minus_result += sum(map(lambda x: int(x.lstrip('0')), i.split('+'))) # 0으로 시작하는 숫자 검증
    else:
      minus_result += int(i)
    
print(result - minus_result)
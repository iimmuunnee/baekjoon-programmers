from sys import stdin

str_arr1 = list(input())
str_arr2 = []
n = int(input())  # 입력받을 명령어 개수
result = ''

for i in range(n):
  order = list(stdin.readline().split())
  if order[0] == 'P':  # 문자열 추가
    str_arr1.append(order[1])

  elif order[0] == 'L':  # 커서를 왼쪽으로 한 칸
    if str_arr1:
      str_arr2.append(str_arr1.pop())
      
  elif order[0] == 'D':  # 커서를 오른쪽으로 한 칸
    if str_arr2:
      str_arr1.append(str_arr2.pop())

  elif order[0] == 'B': # 커서 왼쪽에 있는 문자 삭제
    if str_arr1:
      str_arr1.pop()
    
str_arr1.extend(reversed(str_arr2))
print("".join(str_arr1))
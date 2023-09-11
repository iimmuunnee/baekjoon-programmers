n = int(input())
answer = ''

long_number = n // 4

for i in range(long_number):
  answer += "long "

print(answer + "int")
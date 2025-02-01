import sys

code_list = list(map(int, sys.stdin.readline().split()))
sum = 0
for i in code_list:
  sum += i ** 2

sys.stdout.write(str(sum%10))
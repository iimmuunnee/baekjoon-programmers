import sys

fb_list = [sys.stdin.readline().strip() for i in range(3)]

result = 0

for i in range(3):
  if fb_list[i] not in ["FizzBuzz", "Fizz", "Buzz"]:
    if i == 0:
      result = int(fb_list[i]) + 3
    elif i == 1:
      result = int(fb_list[i]) + 2
    elif i == 2:
      result = int(fb_list[i]) + 1

if result % 3 == 0 and result % 5 == 0:
  result = "FizzBuzz"
elif result % 3 == 0 and result % 5 != 0:
  result = "Fizz"
elif result % 3 != 0 and result % 5 == 0:
  result = "Buzz"
else:
  result = str(result)

sys.stdout.write(result)
while True:
  try:
    n = int(input())
  except:
    break
  num = 0
  i = 1
  while True:
    num = 10 * num + 1
    num %= n
    if num == 0:
      print(i)
      break
    i += 1
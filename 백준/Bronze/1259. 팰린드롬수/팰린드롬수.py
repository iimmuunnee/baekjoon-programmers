import sys

while 1:
  result = "yes"  
  n = sys.stdin.readline().strip()
  if n == "0":
    break
  len_n = len(n)

  for i in range(len_n//2):
    if n[i] == n[len_n - i - 1]:
      continue
    else:
      result = "no"
      break
  sys.stdout.write(result + "\n")
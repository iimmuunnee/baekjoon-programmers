import sys

while 1:
  a, b, c = sorted(map(int, sys.stdin.readline().split()))
  if a == 0 or b == 0 or c == 0:
    break
  a2 = a**2
  b2 = b**2
  c2 = c**2
  if c2 == a2 + b2:
    sys.stdout.write("right \n")
  else:
    sys.stdout.write("wrong \n")
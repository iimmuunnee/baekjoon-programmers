import sys

number = int(sys.stdin.readline())

for i in range(number):
  h, w, n = map(int, sys.stdin.readline().split())
  y = n % h
  if y == 0:
    y = h

  x = (n - 1) // h + 1 # 나누어 떨어질 때 다음 호수로 넘어가는 걸 n-1로 그렇게 함
  str(y)
  str(x)
  sys.stdout.write(f"{y}{x:02d}\n")
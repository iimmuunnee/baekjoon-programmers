import sys

asc = "12345678"
des = "87654321"

n = "".join(sys.stdin.readline().split())
if n == asc:
  sys.stdout.write("ascending")
elif n == des:
  sys.stdout.write("descending")
else:
  sys.stdout.write("mixed")
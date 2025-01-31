a, b = map(int, input().split())
c, d = max(a, b), min(a,b)

def gcd(x, y):
  while y:
    x, y = y, x % y
  return x
num = gcd(c, d)
print(num)
print(int((c * d)/num))
import sys

# a(i) * r**i mod M
r = 31
M = 1234567891
l = int(sys.stdin.readline())
hash_str = sys.stdin.readline()

alphabet_map = {chr(i): i - 96 for i in range(97, 123)}

result = 0
for s in range(l):
  result += alphabet_map[hash_str[s]] * 31**s % M

sys.stdout.write(str(result))
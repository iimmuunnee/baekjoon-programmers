import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result1 = a + b - c
result2 = int(str(a) + str(b)) - c

sys.stdout.write(str(result1) + "\n"
                 + str(result2))
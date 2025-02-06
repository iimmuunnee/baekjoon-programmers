import sys

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

n = int(sys.stdin.readline())

target = str(factorial(n))
cnt = 0

for i in range(len(target) - 1, 0, -1):
    if target[i] == "0":
        cnt += 1
    else:
        break

sys.stdout.write(str(cnt))
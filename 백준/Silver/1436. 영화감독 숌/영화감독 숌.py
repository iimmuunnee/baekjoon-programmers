import sys

cnt = 0
target = 666
n = int(sys.stdin.readline())

while True:
    if "666" in str(target):
        cnt += 1

    if cnt == n:
        break

    target += 1

sys.stdout.write(str(target))
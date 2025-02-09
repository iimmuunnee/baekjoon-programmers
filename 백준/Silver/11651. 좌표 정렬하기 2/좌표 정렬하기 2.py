import sys

n = int(sys.stdin.readline())

coordinate = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

coordinate.sort(key=lambda x: (x[1], x[0]))

for x, y in coordinate:
    sys.stdout.write(f"{x} {y}\n")
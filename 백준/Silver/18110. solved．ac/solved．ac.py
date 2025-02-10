import sys
from decimal import Decimal, ROUND_HALF_UP

input = sys.stdin.readline

n = int(input())

level = [int(input()) for _ in range(n)]
if n == 0:
    print(0)
    sys.exit()

level.sort()

trimmed = int(Decimal(n * 0.15).quantize(Decimal("1"), ROUND_HALF_UP))

if n - 2 * trimmed <= 0:
    sys.stdout.write("0")

else:
    trimmed_level = level[trimmed:n - trimmed]
    avg = Decimal(sum(trimmed_level) / len(trimmed_level)).quantize(Decimal("1"), ROUND_HALF_UP)
    sys.stdout.write(str(avg))
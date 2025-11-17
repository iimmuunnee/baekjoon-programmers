import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

for cwr in combinations_with_replacement([i for i in range(1, n + 1)], m):
    s_cwr = list(map(str, list(cwr)))
    print(" ".join(s_cwr))
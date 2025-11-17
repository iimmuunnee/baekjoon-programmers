import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

perms = list(permutations(n_list, m))
perms.sort()
perms = list(map(list, perms))

for i in perms:
    p = list(map(str, i))
    print(" ".join(p))
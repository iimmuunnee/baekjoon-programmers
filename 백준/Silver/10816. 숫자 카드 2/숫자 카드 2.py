import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

m = int(input())

m_list = list(map(int, input().split()))

counter = Counter(n_list)

result = [str(counter[num]) for num in m_list]

sys.stdout.write(" ".join(map(str, result)))
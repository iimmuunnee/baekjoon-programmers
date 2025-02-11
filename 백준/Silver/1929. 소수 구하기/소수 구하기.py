import sys

input = sys.stdin.readline

m, n = map(int, input().split())

is_prime = [True] * (n + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for multi in range(i ** 2, n + 1, i):
            is_prime[multi] = False

result = [num for num in range(m, n + 1) if is_prime[num]]

for num in result:
    sys.stdout.write(f"{num}\n")
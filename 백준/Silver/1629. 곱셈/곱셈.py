import sys

input = sys.stdin.readline

def multiple(a, b):
    if b == 1:
        return a % c
    else:
        half = multiple(a, b//2)
        if b % 2 == 0:
            return (half * half) % c
        else:
            return (half * half % c * a) % c

a, b, c = map(int, input().split())
print(multiple(a, b))

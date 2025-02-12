import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

unheard = set(input().rstrip() for _ in range(n))

unseen = set(input().rstrip() for _ in range(m))

intersection = list(unheard & unseen)
intersection.sort()

print(str(len(intersection)) + "\n" + "\n".join(intersection))
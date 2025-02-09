import sys

n = int(sys.stdin.readline())

db = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    db.append((int(age), name))

db.sort(key=lambda x: x[0])

for age, name in db:
    sys.stdout.write(f"{age} {name}\n")
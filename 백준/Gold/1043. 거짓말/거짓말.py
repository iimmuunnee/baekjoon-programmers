import sys

input = sys.stdin.readline

# 파티의 대표 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 대표가 같은 파티 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n, m = map(int, input().split())
data = list(map(int, input().split()))
t = data[0]
truth = data[1:]

if t == 0:
    for _ in range(m):
        input()
    print(m)
    exit(0)
    
parent = [i for i in range(n + 1)]
parties = []

for _ in range(m):
    info = list(map(int, input().split()))
    cnt = info[0]
    people = info[1:]
    parties.append(people)
        
    for i in range(1, cnt):
        union(people[0], people[i])

truth_roots = set(find(x) for x in truth)
result = 0

for people in parties:
    if all(find(p) not in truth_roots for p in people):
        result += 1

print(result)

import math
h, w, n, m = map(int, input().split())
# n : 세로 비워
# m : 가로 비워
a = math.ceil(w/(m+1))
b = math.ceil(h/(n+1))
answer = a * b
print(answer)

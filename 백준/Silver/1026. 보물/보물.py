s = 0
n = int(input())
a = map(int, input().split(" ")) # a 배열
b = map(int, input().split(" ")) # b 배열 

sorted_a = sorted(a)
sorted_b = sorted(b, reverse=True)

for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)
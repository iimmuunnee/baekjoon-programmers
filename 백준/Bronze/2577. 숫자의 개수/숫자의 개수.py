a = int(input())
b = int(input())
c = int(input())
cnt_num = {}

abc = a * b * c
str_abc = str(abc)

for i in range(10):
    cnt_num[i] = 0

for i in str_abc:
    cnt_num[int(i)] = cnt_num[int(i)] + 1

for i in range(10):
    print(cnt_num[i])
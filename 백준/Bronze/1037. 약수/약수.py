n = int(input())
n_list = list(map(int, input().split(" ")))

if n == 1:
    print(n_list[0]**2)
else:
    print(max(n_list) * min(n_list))
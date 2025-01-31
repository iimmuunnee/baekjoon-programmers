n = int(input())
n_list = list(map(int, input().split(" ")))

if n == 1:
    print(n_list[0] ** 2)
else:
    max_val, min_val = n_list[0], n_list[0]  # 첫 번째 요소를 기준으로 최댓값과 최솟값을 설정
    for num in n_list[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(max_val * min_val)
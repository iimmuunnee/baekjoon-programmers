import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

input_list = [input().rstrip() for _ in range(n+m)]

pokedex = input_list[0:n]
name_to_num = {pokedex[i]: i+1 for i in range(n)}
q_list = input_list[n:n+m+1]

for i in q_list:
    if i.isalpha(): # 문자열이면
        sys.stdout.write(f"{name_to_num[i]}\n")
    elif i.isdigit(): # 숫자면
        sys.stdout.write(f"{pokedex[int(i) - 1]}\n")

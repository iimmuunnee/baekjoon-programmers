import sys


input = sys.stdin.readline

k = int(input())

num_list = []

for _ in range(k):
    num = int(input())
    
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()

sys.stdout.write(str(sum(num_list)))
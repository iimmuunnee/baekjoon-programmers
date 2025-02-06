import sys

n = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline().strip()) for i in range(n)]
num_list.sort()

for num in num_list:
    sys.stdout.write(str(num) + "\n")
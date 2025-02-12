import sys

input = sys.stdin.readline

zero_count = list(0 for _ in range(40+1))
one_count = list(0 for _ in range(40+1))

zero_count[0] = 1
one_count[1] = 1

n = int(input().strip())

for _ in range(n):
    num = int(input().strip())
    if num >= 2:
        for i in range(2, num+1):
            zero_count[i] = zero_count[i-1] + zero_count[i-2]
            one_count[i] = one_count[i-1] + one_count[i-2]
    
    sys.stdout.write(f"{zero_count[num]} {one_count[num]}\n")
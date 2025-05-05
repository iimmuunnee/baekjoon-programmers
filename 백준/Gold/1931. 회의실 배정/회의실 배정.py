import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

end_time = 0 # 가장 최근 회의의 끝난 시간
count = 0

for start, end in arr:
    if start >= end_time:
        count += 1
        end_time = end

sys.stdout.write(str(count))
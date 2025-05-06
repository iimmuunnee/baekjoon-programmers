import sys

n = int(sys.stdin.readline()) # n + 1개의 I, n개의 O
m = int(sys.stdin.readline()) # S의 길이
s = sys.stdin.readline() # 주어진 문자열

i = 0
cnt = 0
pn_cnt = 0

while i < m - 1:
    if s[i] == "I" and s[i+1] == "O":
        pn_cnt = 0

        while i + 2 < m and s[i+1] == "O" and s[i+2] == "I":
            pn_cnt += 1
            i += 2

            if pn_cnt >= n:
                cnt += 1

        i += 1
    else:
        i += 1

sys.stdout.write(str(cnt))
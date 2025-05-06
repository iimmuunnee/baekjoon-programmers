import sys
import re

n = int(sys.stdin.readline()) # n + 1개의 I, n개의 O
m = int(sys.stdin.readline()) # S의 길이
s = sys.stdin.readline() # 주어진 문자열

Pn = "IO" * n + "I" # n번째 문자열 형태
cnt = 0

# 직접 구현
for i in range(m - len(Pn) + 1):
    if s[i:i+len(Pn)] == Pn:
        cnt += 1

# re 라이브러리 사용
matches = re.findall(f"(?={Pn})", s)
cnt = len(matches)

sys.stdout.write(str(cnt))
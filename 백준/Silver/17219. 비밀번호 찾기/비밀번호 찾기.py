import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # n과 m 입력력

site_password = dict(input().strip().split() for _ in range(n)) # 사이트와 비밀번호 딕셔너리 입력 및 생성성

for _ in range(m): # 찾고싶은 사이트의 비밀번호 입력 및 출력력
    site = input().strip()
    sys.stdout.write(f"{site_password[site]}\n")
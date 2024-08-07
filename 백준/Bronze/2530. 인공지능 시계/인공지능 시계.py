a, b, c = map(int, input().split())  
time = int(input())

m_time = time // 60 # 몫 = 분
s_time = time % 60 # 나머지 = 초

b += m_time
c += s_time

if c >= 60:
  b += c // 60
  c %= 60
if b >= 60:
  a += b // 60
  b %= 60
if a >= 24:
  a %= 24

print(a, b, c)
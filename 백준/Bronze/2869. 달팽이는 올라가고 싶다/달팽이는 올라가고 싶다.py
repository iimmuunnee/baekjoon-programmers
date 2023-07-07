a, b, v = map(int, input().split(" "))
day = 0

up = v - a # 마지막 날 제외
day_up = a - b # 하루에 올라가는 길이

if up % day_up == 0:
    day = up // day_up + 1 # 1: 마지막 날
else:
    day = up // day_up + 2 # 2: 마지막날 + 나머지 길이올라가는 날

print(day)
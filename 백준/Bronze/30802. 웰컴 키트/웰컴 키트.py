import sys

N = int(sys.stdin.readline()) # 참가자 수
shirt_list = list(map(int, sys.stdin.readline().split())) # 티셔츠 사이즈별 신청자의 수
T, P = map(int, sys.stdin.readline().split()) # T: 티셔츠의 주문 묶음 수, P: 펜의 주문 묶음 수

t_number = 0
p_number = 0

for i in shirt_list:
  if i % T != 0:
    t_number += i // T + 1
  else:
    t_number += i // T

p_number1 = N // P
p_number2 = N % P

sys.stdout.write(str(t_number) + "\n")
sys.stdout.write(str(p_number1) + " " + str(p_number2))
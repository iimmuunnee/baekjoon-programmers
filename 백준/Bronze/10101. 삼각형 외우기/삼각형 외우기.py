a = int(input())  # 삼각형의 각 1
b = int(input())  # 삼각형의 각 2
c = int(input())  # 삼각형의 각 3


if(a + b + c == 180):
  if (a == b and b == c):
    print("Equilateral")
  elif(a == b or b == c or a == c):
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")
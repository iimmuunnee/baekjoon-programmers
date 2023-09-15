while True:
  a, b, c = map(int, input().split())
  array = [a, b, c]
  max_k = max(array)
  array.remove(max_k)
  if(a != 0 or b != 0 or c != 0):
    if(sum(array) > max_k): # 삼각형의 조건 만족
      if(a == b and b == c):
        print("Equilateral")
      elif(a == b or b == c or a == c):
        print("Isosceles ")
      else:
        print("Scalene ")
    else:
      print("Invalid")  
  
  else: # 종료
    break
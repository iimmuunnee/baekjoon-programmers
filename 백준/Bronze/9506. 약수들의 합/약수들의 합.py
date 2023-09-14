array = []
result = ""

while True:
  n = int(input())
  if(n == -1):
    break
  for i in range(1, n):
    if(n%i == 0):
      array.append(i)
  if(n != sum(array)):
    print(f'{n} is NOT perfect.')
    array=[]
  else:
    for i in range(len(array)):
      if(i == len(array) - 1):
        result += f'{array[i]}'
        print(f'{n} = {result}')
        result=""
        array=[]
      else:
        result += f'{array[i]} + '
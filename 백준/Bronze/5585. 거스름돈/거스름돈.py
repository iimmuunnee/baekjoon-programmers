pay = int(input()) # 지불할 돈
change = 1000 - pay # 거스름돈
result = 0 # 동전 개수
coin_arr = [500, 100, 50, 10, 5, 1]

for coin in coin_arr:
  result += change // coin
  change %= coin

print(result)
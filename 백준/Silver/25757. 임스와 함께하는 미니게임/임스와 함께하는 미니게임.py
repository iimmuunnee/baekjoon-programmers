n, k = input().split()
user = set()
for i in range(int(n)):
    user.add(input())

u = len(user)
if k == "Y": # 윷놀이 2
    print(u)
elif k == "F": # 같은 그림찾기 3
    print(u//2)
elif k == "O": # 원카드 4
    print(u//3)

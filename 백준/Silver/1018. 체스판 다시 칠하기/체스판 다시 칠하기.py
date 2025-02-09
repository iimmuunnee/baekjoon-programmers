import sys

input = sys.stdin.readline

m, n = map(int, input().split())
board = [input().strip() for _ in range(m)]

repaint = float('inf')

for i in range(m -7): # 보드를 만들 수 있는 행의 범위
    for j in range(n - 7): # 보드를 만들 수 있는 열의 범위
        count1 = 0 # 왼쪽 위가 W
        count2 = 0 # 왼쪽 위가 B

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                current_color = board[x][y]

                if (x + y) % 2 == 0: # 좌표의 합이 짝수일 때 
                    # 왼쪽 위가 W일 때 좌표의 합이 짝수 => W, 홀수 => B
                    if current_color != "W":
                        count1 += 1
                    # 왼쪽 위가 B일 대 좌표의 합이 짝수 => B, 홀수 => W
                    if current_color != "B":
                        count2 += 1

                else: # 좌표의 합이 홀수일 때
                    if current_color != "B":
                        count1 += 1
                    
                    if current_color != "W":
                        count2 += 1
        repaint = min(repaint, count1, count2)

sys.stdout.write(str(repaint))
import sys

input = sys.stdin.readline

white = 0
blue = 0

def devide(x, y, size):
    global white, blue

    first_color = square[x][y]
    is_same = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if square[i][j] != first_color:
                is_same = False
                break
        if not is_same: # 색이 같지 않음
            break
    

    if is_same:
        if first_color == 0:
            white += 1
        else:
            blue += 1
        return
    
    half = size // 2
    devide(x, y, half)
    devide(x+half, y, half)
    devide(x, y+half, half)
    devide(x+half, y+half, half)

n = int(input()) # 종이의 한 변의 길이
square = [list(map(int, input().rstrip().split())) for _ in range(n)]

devide(0, 0, n)

print(white)
print(blue)

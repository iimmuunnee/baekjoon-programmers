def solution(keyinput, board):
    answer = [0, 0]
    max_row = (board[0] - 1) / 2
    max_column = (board[1] - 1) / 2
    for i in keyinput:
        if i == "right":
            if answer[0] != max_row:
                answer[0] += 1
        elif i == "left":  
            if answer[0] != -max_row:
                answer[0] -= 1
        elif i == "up":
            if answer[1] != max_column:
                answer[1] += 1                
        elif i == "down":
            if answer[1] != -max_column:
                answer[1] -= 1
        
    return answer
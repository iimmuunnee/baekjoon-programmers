def solution(board, moves):
    answer = 0
    result = []
    r = len(board) # 행
    c = len(board[0]) # 열
    for num in moves:
        for i in range(r):
            if board[i][num - 1] == 0:
                continue
            else:
                result.append(board[i][num - 1])
                board[i][num - 1] = 0
                if len(result) > 1:
                    if result[-1] == result[-2]:
                        result.pop(-1)
                        result.pop(-1)
                        answer += 2
            break
    return answer
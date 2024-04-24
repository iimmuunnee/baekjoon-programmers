def solution(my_str, n):
    answer = []
    len_str = len(my_str)
    for i in range(len_str//n): # 0 1 
        answer.append(my_str[(i)*n : (i+1)*n])
    if len_str % n != 0:
        answer.append(my_str[(len_str//n)*n:])
    return answer
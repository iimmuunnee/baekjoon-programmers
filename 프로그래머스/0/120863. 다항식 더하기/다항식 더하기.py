def solution(polynomial):
    answer = [0, 0]
    result = ""
    poly_list = polynomial.split(" ")
    for i in range(0, len(poly_list), 2):
        if "x" in poly_list[i]:
            if len(poly_list[i]) >= 2:
                answer[0] += int(poly_list[i][:-1])
            else:
                answer[0] += 1
        else:
            answer[1] += int(poly_list[i])
            
    if answer[0] >= 2:
        answer[0] = str(answer[0]) + "x"
    elif answer[0] == 1:
        answer[0] = "x"
        
    answer[0] = str(answer[0])
    answer[1] = str(answer[1])
    
    if answer[1] == "0":
        return answer[0]
    elif answer[0] == "0":
        return answer[1]
    else:
        return " + ".join(answer)
        
                
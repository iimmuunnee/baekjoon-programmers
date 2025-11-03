def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        p_list = []
        p_bool = True
        for c in s:
            if c in ["[", "(", "{"]:
                p_list.append(c)
            else:
                if c == "]":
                    if "[" in p_list:
                        if "[" == p_list[-1]:
                            p_list.pop()
                        else:
                            break
                            p_bool = False
                    else:
                        p_bool = False
                        break
                elif c == ")":
                    if "(" in p_list:
                        if "(" == p_list[-1]:
                            p_list.pop()
                        else:
                            break
                            p_bool = False
                    else:
                        p_bool = False
                        break
                elif c == "}":
                    if "{" in p_list:
                        if "{" == p_list[-1]:
                            p_list.pop()
                        else:
                            break
                            p_bool = False
                    else:
                        p_bool = False
                        break

        if not p_list and p_bool:
            print("+1")
            answer += 1
        s = s[1:] + s[0]  # 왼쪽 rotate

    return answer
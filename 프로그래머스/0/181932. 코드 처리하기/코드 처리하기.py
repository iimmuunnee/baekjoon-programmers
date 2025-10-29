def solution(code):
    answer = ''
    mode = "0"
    for i, c in enumerate(code):
        if c == "1":
            if mode == "0":
                mode = "1"
                continue
            else:
                mode = "0"
                continue
        # print(f"c={c} i={i} mode={mode}")
        if mode == "0":
            if i % 2 == 0:
                answer += code[i]
        elif mode == "1":
            # print("mode = 1")
            if i % 2 == 1:
                answer += code[i]
    if answer == "":
        answer = "EMPTY"
    return answer
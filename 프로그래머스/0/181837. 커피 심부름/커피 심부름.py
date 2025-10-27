def solution(order):
    answer = 0
    ame, latte = 0, 0
    print(order)
    for w in order:
        if "americano" in w or w == "anything":
            ame += 1
        elif "latte" in w:
            latte += 1
    answer = ame * 4500 + latte * 5000
            
    return answer
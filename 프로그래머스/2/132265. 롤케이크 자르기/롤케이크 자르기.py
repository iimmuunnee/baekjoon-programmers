from collections import Counter

def solution(topping):
    answer = 0
    right = Counter(topping)
    print(right)
    left = set()
    
    for t in topping[:-1]:
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        left.add(t)
        
        if len(right) == len(left):
            answer += 1

    return answer
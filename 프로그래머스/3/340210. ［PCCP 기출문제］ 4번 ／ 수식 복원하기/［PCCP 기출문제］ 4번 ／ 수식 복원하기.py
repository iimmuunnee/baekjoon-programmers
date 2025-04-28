
def is_valid(str_num, base):
    try:
        int(str_num, base)
        return True
    except ValueError:
        return False

def to_base(num, base):
    if num == 0:
        return "0"
    
    res =  ""
    while num:
        res = str(num % base) + res
        num //= base
        
    return res
    
def solution(expressions):
    answer = []
    
    max_digit = 0
    for expr in expressions:
        parts = expr.replace("=", " ").replace("+", " ").replace("-", " ").split()
        for p in parts:
            for ch in p:
                if ch.isdigit():
                    max_digit = max(int(ch), max_digit)
    
    min_base = max_digit + 1
    
    possible_base = []
    
    for base in range(min_base, 10):
        valid = True
        
        for expr in expressions:
            if "X" in expr:
                continue
            
            a, op, b, _, c = expr.split()
            if not (is_valid(a, base) and is_valid(b, base) and is_valid(c, base)):
                vaild = False
                break
            
            a_val = int(a, base)
            b_val = int(b, base)
            c_val = int(c, base)
            
            if op == "+":
                if a_val + b_val != c_val:
                    valid = False
                    break
            elif op == "-":
                if a_val - b_val != c_val:
                    valid = False
                    break
            
        if valid:
            possible_base.append(base)
    
    for expr in expressions:
        if "X" not in expr:
            continue
        
        a, op, b, _, _ = expr.split()
        result = set()
        
        # 가능한 진수중에 값이 같은지 안 같은지
        for base in possible_base:
            if not (is_valid(a, base) and is_valid(b, base)):
                continue
            
            a_val = int(a, base)
            b_val = int(b, base)
            
            if op == "+":
                x_val = a_val + b_val
            elif op == "-":
                x_val = a_val - b_val
            
            result.add(to_base(x_val, base))
        
        if len(result) == 1:
            c = result.pop()
            answer.append(f"{a} {op} {b} = {c}")
        else: # 여러 진수에서 되지만 각각의 값이 다를 경우는 물음표(?)로 처리
            answer.append(f"{a} {op} {b} = ?")
        
            
    return answer
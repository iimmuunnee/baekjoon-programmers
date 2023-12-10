def solution(number, k):
    # 가장 작은 숫자로 정렬 후 그 숫자만 pop 해서 없애기
    answer = ''
    result = [] # 큰 수 모음
    for num in number:
        if not result:
            result.append(num)
            continue
        if k > 0:
            while result[-1] < num:
                result.pop()
                k -= 1
                if not result or k <= 0:
                    break
        result.append(num)
    result = result[:-k] if k > 0 else result
    answer = "".join(result)
    return answer
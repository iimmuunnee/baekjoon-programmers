def solution(picture, k):
    # k가 3이라면 기존의 인덱스에서 k-1만큼까지 차지함 0 ~ 2, 3 ~ 5, 6 ~ 8
    # 다음 행과 열의 인덱스는 기존 인덱스에서 * k
    x, y = len(picture), len(picture[0]) # 행, 열
    answer = []
    
    for s in picture:
        new_str = ""
        for c in s:
            new_str += c * k
        for _ in range(k):
            answer.append(new_str)
    
    return answer
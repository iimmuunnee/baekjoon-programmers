def solution(genres, plays):
    answer = []
    cate = {}
    temp = []
    
    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    temp = sorted(temp, key = lambda x: (x[0], -x[1], x[2])) # 재생 수 내림차순, 고유번호 오름차순
    
    for idx, genre in enumerate(genres):
        cate[genre] = cate.get(genre, 0) + plays[idx] 
    sorted_value = sorted(cate.items(), key = lambda x:x[1], reverse=True)
    
    for i in sorted_value: # 같은 장르 2곡 추출
        count = 0
        for j in temp:
            if i[0] == j[0]:
                count +=1 
                if count > 2:
                    break
                else :
                    answer.append(j[2])

    return answer
def solution(phone_book):
    answer = True
    phone_book.sort() # 정렬하는 이유는 시작하는 숫자가 동일해야 의미가 있기때문
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    return answer
def solution(n, words):
    answer = [0, 0]
    used_words = set()  # 이미 사용된 단어를 저장하는 집합
    last_char = words[0][0]  # 첫 번째 단어의 첫 글자로 시작

    for idx, word in enumerate(words):
        if word in used_words or word[0] != last_char or len(word) == 1:
            # 이미 사용된 단어, 끝말잇기 규칙 위반, 한 글자인 단어
            answer = [(idx % n) + 1, (idx // n) + 1] # 차례, 라운드
            break

        used_words.add(word)
        last_char = word[-1]

    return answer

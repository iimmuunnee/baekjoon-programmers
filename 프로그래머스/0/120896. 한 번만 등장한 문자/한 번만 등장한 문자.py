def solution(s):
    answer = ''
    set_s = "".join(dict.fromkeys(s))
    answer_list = [i for i in set_s if s.count(i) == 1]
    answer_list.sort()
    answer = "".join(answer_list)
    return answer 
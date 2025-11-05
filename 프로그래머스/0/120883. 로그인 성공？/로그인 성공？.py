def solution(id_pw, db):
    answer = 'fail'
    for db_id, db_pw in db:
        if id_pw[0] == db_id:
            if id_pw[1] == db_pw:
                answer = "login"
                break
            else:
                answer = "wrong pw"
                break
                
    return answer
def solution(id_pw, db):
    for user in db:
        if user[0] == id_pw[0]:
            return "login" if user[1] == id_pw[1] else "wrong pw"
    return "fail"
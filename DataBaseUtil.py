import pymysql


class dataBaseUtil:
    connect = None

    def __init__(self, host, port, user, pwd, db):
        self.connect = pymysql.connect(user=user, password=pwd, host=host, port=port, database=db, charset="utf8")


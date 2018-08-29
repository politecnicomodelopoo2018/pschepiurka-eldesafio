import pymysql


class DB(object):
    __instance = None
    __HOST = 'localhost'
    __USER = 'root'
    __PASSWD = 'alumno'
    __DB = 'LaboTP2'

    def __new__(cls, *args, **kwargs):
        if DB.__instance is None:
            DB.__instance = object.__new__(cls)
        return DB.__instance

    def run(self, query):
        db = pymysql.connect(host=self.__HOST,
                             user=self.__USER,
                             passwd=self.__PASSWD,
                             db=self.__DB,
                             charset="utf8",
                             autocommit=True)

        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(query)
        db.close()

        return cursor

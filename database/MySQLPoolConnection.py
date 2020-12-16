import pymysql
from pymysqlpool.pool import Pool
from serverConstants.ServerSettings import ServerInfoSetting
from importLib.ErrorLib import *

pool = Pool(host=ServerInfoSetting.DB_HOST,
            port=ServerInfoSetting.DB_PORT,
            user=ServerInfoSetting.DB_USER,
            password=ServerInfoSetting.DB_PASSWORD,
            db=ServerInfoSetting.DB_NAME,
            autocommit=ServerInfoSetting.DB_AUTO_COMMIT,
            max_size=ServerInfoSetting.DB_MAX_POOL_SIZE,
            timeout=ServerInfoSetting.DB_TIMEOUT,
            min_size=1)


class SQLConnection:
    @staticmethod
    def getConnection():
        global pool
        try:
            if ServerInfoSetting.SHOW_POOL_LOG:
                print('POOL SIZE ' + str(pool.get_pool_size()))  # TODO: POOL SIZE
            return pool.get_conn()
        except Exception as e:
            LogCat.log(ErrLevel.unknown,traceback.format_exc())


class MySQLPool:
    def __init__(self,conn):
        self.conn = conn
        self.curs = None

    def __del__(self):
        if self.conn is not None:
            pool.release(self.conn)

    def executeSQL(self, sql):
        global pool
        try:
            self.curs = self.conn.cursor()
            self.curs.execute(sql)
        except pymysql.err.OperationalError as e:
            pool = Pool(host=ServerInfoSetting.DB_HOST,
                        port=ServerInfoSetting.DB_PORT,
                        user=ServerInfoSetting.DB_USER,
                        password=ServerInfoSetting.DB_PASSWORD,
                        db=ServerInfoSetting.DB_NAME,
                        autocommit=ServerInfoSetting.DB_AUTO_COMMIT,
                        max_size=ServerInfoSetting.DB_MAX_POOL_SIZE,
                        timeout=ServerInfoSetting.DB_TIMEOUT,
                        min_size=1)
        except Exception as e:
            LogCat.log(ErrLevel.unknown,traceback.format_exc())
            raise e

    def getQueryData(self,option = 0): # (Feat. 김준석)
        if option != 1:
            data = self.curs.fetchall()
        else:
            data = self.curs.fetchone()
        if data is None:
            return None
        return data if len(data) != 0 else None

    def close(self):
        pool.release(self.conn)
        self.conn = None

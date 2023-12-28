
import redis
import pymysql


class Check():
    @staticmethod
    def check_redis():
        try:
            r = redis.Redis(host='localhost', port=6379)
            r.ping()
            print("Redis已啟動")
        except redis.ConnectionError:
            print("Redis未啟動")

    @staticmethod
    def init_sql():
        # SQL 初始化
        pymysql.install_as_MySQLdb()

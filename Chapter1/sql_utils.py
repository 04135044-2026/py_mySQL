
import pymysql
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

class Sqlutils:
    #db_query = "show databases;"

    def __init__(self):
        self.connection = pymysql.connect(
            host= config['DB']['host'],
            user=config['DB']['user'],
            password=config['DB']['password'],
            port=int(config['DB']['port']),
            cursorclass=pymysql.cursors.DictCursor,
        )

    def sql_query(self,query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        return result

    def show_dbs(self):
        with self.connection.cursor() as cursor:  
            cursor.execute("SHOW DATABASES")
            result = cursor.fetchall()

        return result



import pymysql
import configparser 

config = configparser.ConfigParser()
config.read('../Chapter1/config.ini')

# 特例 -> 因為 create database 不能帶入字串
def create_database(database):
    connection = pymysql.connect(
        host=config.get('DB', 'host'),
        user=config.get('DB', 'user'),
        password=config.get('DB', 'password'),
        port=config.getint('DB', 'port'),
        cursorclass=pymysql.cursors.DictCursor,
    )
    with connection.cursor() as cursor:
        sql = f"""
        create database if not exists {database};
                """
    # 執行建立的 SQL 語句
    cursor.execute(sql)
    # 執行查看資料庫
    cursor.execute("show databases;")
    dbs = cursor.fetchall()

    print(dbs)


def create_user_table(database):
    connection = pymysql.connect(
        host=config.get('DB', 'host'),
        user=config.get('DB', 'user'),
        password=config.get('DB', 'password'),
        port=config.getint('DB', 'port'),
        cursorclass=pymysql.cursors.DictCursor,
        database=database,
    )
    
    with connection.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(250) NOT NULL,
            age INT,
            username VARCHAR(250) NOT NULL UNIQUE,
            password VARCHAR(20) NOT NULL
        );
    """
        cursor.execute(sql)
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
    print(tables)

# 建立寫入使用者的 function

def create_user(name, age, username, password, database='chapter2'):
     connection = pymysql.connect(
        host=config.get('DB', 'host'),
        user=config.get('DB', 'user'),
        password=config.get('DB', 'password'),
        port=config.getint('DB', 'port'),
        cursorclass=pymysql.cursors.DictCursor,
        database=database,
    )
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO user(name, age, username, password)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (name, age, username, password))
        
        cursor.execute("SELECT * FROM user WHERE username = %s;", (username))  
        r = cursor.fetchall
        print(r)
    connection.commit()

    connection.close()
import pymysql
import pymysql.cursors
from config import Config

def get_Connection():
    connection = pymysql.connect(
        host=Config.mysql_host,
        port=Config.mysql_port,
        user=Config.mysql_user,
        password=Config.mysql_password,
        db=Config.mysql_db,
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8mb4',
        autocommit=False
    )
    return connection


def execute_sql(sql: str, params: tuple = (), fetchone: bool = False, fetchall: bool = False, commit: bool = False):
    conn = get_Connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            if commit:
                conn.commit()
                return cursor.lastrowid
            if fetchone:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()
    except Exception:
            conn.rollback()
            raise
    finally:
        conn.close()
    
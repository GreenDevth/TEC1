from mysql.connector import MySQLConnection, Error
from database.db_config import read_db_config

db = read_db_config()

def check_queue():
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('select count(*) from scum_shopping_cart')
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            return res[0]
    except Error as e:
        print(e)


def get_pack(order):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('select package_name from scum_shopping_cart where order_number = %s', (order,))
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            return res[0]
    except Error as e:
        print(e)
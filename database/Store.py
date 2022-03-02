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


def get_queue(product_code):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('SELECT steam_id, package_name FROM scum_shopping_cart WHERE order_number = %s', (product_code,))
        row = cur.fetchone()
        while row is not None:
            data = list(row)
            return data
    except Error as e:
        print(e)


def get_package(pack_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT package_data FROM scum_package WHERE package_name = %s', (pack_name,))
        row = cur.fetchone()
        while row is not None:
            data = list(row)
            return data[0]
    except Error as e:
        print(e)


def delete_row():
    conn = None
    try:
        dbconfi = read_db_config()
        conn = MySQLConnection(**dbconfi)
        cur = conn.cursor()
        cur.execute('DELETE FROM scum_shopping_cart LIMIT 1')
        conn.commit()
        cur.close()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
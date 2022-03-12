from mysql.connector import MySQLConnection, Error
from database.db_config import read_db_config

db = read_db_config()


def get_daily_pack_from_shopping_cart(ordernumber):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('SELECT steam_id, item_id FROM scum_shopping_cart WHERE order_number = %s', (ordernumber,))
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            return res
    except Error as e:
        print(e)


def get_dailypack_spawner_code(itemid):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('SELECT spawner_code FROM scum_items WHERE item_id = %s', (itemid,))
        row = cur.fetchone()
        while row is not None:
            data = list(row)
            return data[0]
    except Error as e:
        print(e)
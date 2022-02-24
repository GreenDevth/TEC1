from mysql.connector import MySQLConnection, Error
from db.mysql_dbconfig import read_db_config


def check_steam_exists(discord_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT steam_id FROM scum_shopping_cart WHERE  discord_id = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            steam_id = list(row)
            return steam_id[0]
    except Error as e:
        print(e)


def check_queue():
    """Count Queue for Shopping Cart"""
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM scum_shopping_cart')
        row = cur.fetchone()
        while row is None:
            queue = 0
            return queue
        while row is not None:
            queue = list(row)
            return queue[0]
    except Error as e:
        print(e)


def in_Order(discord_id):
    """Count product_code from current discord id"""
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT COUNT(product_code) FROM scum_shopping_cart WHERE discord_id = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            order = list(row)
            return order[0]
    except Error as e:
        print(e)


def Order_add(discord_id, discord_name, steam_id, product_code, package_name):
    """Add Order in scum_shopping_cart by discord_id"""
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO scum_shopping_cart(discord_id, discord_name, steam_id, product_code, package_name) VALUES (%s,%s,%s,%s,%s)',
            (discord_id, discord_name, steam_id, product_code, package_name))
        conn.commit()
        print('Insert new order name {}'.format(product_code))
        cur.close()
        total_queue = check_queue()
        current_order = in_Order(discord_id)
        msg = "คำสั่งหมายเลข {0} กำลังดำเนินการจัดส่งให้คุณ จาก {1}/{2} คิว".format(product_code, current_order,
                                                                                    total_queue)
        return msg.strip()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()

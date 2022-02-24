from mysql.connector import MySQLConnection, Error
from db.mysql_dbconfig import read_db_config


def get_pack(pack_name):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select package_data from scum_package where package_name = %s', (pack_name,))
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            pack = res[0]
            return pack
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()




















def check_queue():
    conn = None
    try:
        dbconfig = read_db_config()
        connection = MySQLConnection(**dbconfig)
        conn = connection
        cur = conn.cursor()
        cur.execute('select count(*) from scum_shopping_cart')
        row = cur.fetchone()
        while row is None:
            queue = "0"
            return queue.strip()
        while row is not None:
            queue = list(row)
            return queue[0]
        print(row)

    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def check_steam_exists(discord_id):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select steam_id from scum_shopping_cart where discord_id = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            return row
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def in_order(discord_id):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select count(product_code) from scum_shopping_cart where discord_id = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            order = list(row)
            return order[0]
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def Order_add(discord_id, steam_id, product_code, discord_name):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute(
            'insert into scum_shopping_cart(discord_id, steam_id, product_code, discord_name) values(%s,%s,%s,%s)',
            (discord_id, steam_id, product_code, discord_name,))
        conn.commit()
        print('Insert New Order name : {}'.format(product_code))
        cur.close()
        total_queue = check_queue()
        your_order = in_order(discord_id)
        msg = "คำสั่งเลขที่ {0} กำลังดำเนินการจัดส่งให้คุณ จาก {1}/{2} queue.".format(product_code, your_order,
                                                                                      total_queue)
        return msg.strip()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def count_team(team):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT COUNT(team) FROM scum_events WHERE team = %s', (team,))
        counts = cur.fetchone()
        while counts is not None:
            result = list(counts)
            count = result[0]
            return count

    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def count_queue():
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM scum_shopping_cart')
        counts = cur.fetchone()
        queue = list(counts)
        return queue[0]
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def check_steam_id(discord_id):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select steam_id from scum_players where discord_id =%s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            steam_id = list(row)
            return steam_id[0]
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def get_me_queue(discord_id):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select * from scum_shopping_cart where discord_id = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            result = list(row)
            return result
    except Error as e:
        print(e)


def check_exists(discord_id):
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select steam_id from scum_shopping_cart where discord_id = %s', (discord_id,))
        row = cur.tetchone()
        while row is not None:
            row = 1
            return row
        while row is None:
            row = 0
            return row
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
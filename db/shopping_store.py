from mysql.connector import MySQLConnection, Error
from db.mysql_dbconfig import read_db_config


def buy(discord_id, price):
    """Player buy in process"""
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT COINS FROM scum_players WHERE DISCORD_ID = %s', (discord_id,))
        row = cur.fetchone()
        while row is None:
            msg = "ขออภัยไม่พบบัญชีผู้เล่นนี้ในระบบ"
            return msg.strip()
        while row is not None:
            data = list(row)
            check = data[0]
            coins = "${:,d}".format(check)
            if check < price:
                msg = "คุณมียอดเงินคงเหลือไม่เพียงพอสำหรับการสั่งซื้อ```css\nยอดเงินในบัญชีของคุณคือ {} \n```".format(coins)
                return msg.strip()
            if price < check:
                coin = check - price
                cur.execute('UPDATE scum_players SET COINS = %s WHERE DISCORD_ID = %s', (coin, discord_id,))
                conn.commit()
                cur.close()
                msg = "ระบบกำลังจัดส่งรายการสั่งซื้อของคุณ โปรดตรวจสอบให้แน่ใจว่ากำลังออนเกมส์อยู่```css\nยอดเงินคงเหลือคือ {}\n```".format(coins)
                return msg.strip()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def checkout():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT steam_id, product_code FROM scum_shopping_cart LIMIT 1')
        row = cur.fetchall()
        row = list(row)
        return row
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


def get_steam_id(discord_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT steam_id FROM scum_players WHERE DISCORD_ID = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            data = list(row)
            steam_id = data[0]
            return steam_id
        while row is None:
            msg = "ไม่พบข้อมูลผู้เล่นของคุณในระบบ โปรดตอบสอบให้แน่ใจว่าคุณได้ลงทะเบียน Steam id ไว้กับระบบแล้วหรือยัง"
            return msg.strip()
    except Error as e:
        print(e)


def reset_shopping_cart():
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('TRUNCATE TABLE scum_shopping_cart')
        conn.commit()
        cur.close()
        msg = "📢 ระบบทำการ ล้างข้อมูล scum_shopping_cart เรียบร้อยแล้ว"
        return msg.strip()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def get_package(pack_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT package_data FROM scum_package WHERE package_name = %s', (pack_name,))
        row = cur.fetchone()
        while row is None:
            msg = "ไม่มีคำสั่งนี้ในระบบ"
            return msg.strip()
        while row is not None:
            data = list(row)
            return data[0]
    except Error as e:
        print(e)


def get_queue(product_code):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT steam_id, package_name FROM scum_shopping_cart WHERE product_code = %s', (product_code,))
        row = cur.fetchone()
        while row is None:
            msg = 'ไมพบ Product Code {} ในระบบ'.format(product_code)
            return msg.strip()
        while row is not None:
            data = list(row)
            return data
    except Error as e:
        print(e)
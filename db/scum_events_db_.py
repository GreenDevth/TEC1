from mysql.connector import MySQLConnection, Error
from db.mysql_dbconfig import read_db_config


def get_location():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('SELECT commands FROM scum_location_events WHERE status = 0 LIMIT 1')
        row = cur.fetchone()
        while row is not None:
            location = list(row)
            return location[0]
    except Error as e:
        print(e)


def update_status():
    conn = None
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('UPDATE scum_location_events SET status = 1 WHERE  status = 0 LIMIT 1')
        conn.commit()
        msg = "ระบบกำลังส่งคุณไปยังตำแหน่งของ Events เพื่อรับของเริ่มต้น"
        return msg.strip()
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
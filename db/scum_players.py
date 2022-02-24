from mysql.connector import MySQLConnection, Error
from db.mysql_dbconfig import read_db_config


def get_steam_id(discord_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute('select steam_id from scum_players where discord_id = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            return res[0]
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
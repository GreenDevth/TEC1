from mysql.connector import MySQLConnection, Error
from database.db_config import read_db_config

db = read_db_config()


def players_info(discord_id):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('SELECT STEAM_ID FROM scum_players WHERE DISCORD_ID = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            res = list(row)
            return res[0]
    except Error as e:
        print(e)

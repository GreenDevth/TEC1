from ast import While
import time
import pyautogui as ai
import pygetwindow as gw
from mysql.connector import MySQLConnection, Error
from database.db_config import read_db_config
from database.Store import check_queue, get_pack
db = read_db_config()

def start_game():
    time.sleep(1)
    icon = './img/icon.PNG'
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
    ai.moveTo(scum)
    ai.doubleClick(scum)
    msg = "กำลังเริ่มเกมส์ โปรดรอสักครู่"
    return msg.strip()


def login_game():
    time.sleep(1)
    login = "./img/login.PNG"
    scum = ai.locateOnScreen(login, grayscale=True, confidence=0.5)
    ai.moveTo(scum)
    ai.click(scum)
    ai.mouseDown(button='left')
    ai.moveTo(30, 15)
    win = gw.getWindowsWithTitle('SCUM')[0]
    win.resizeTo(640, 400)
    time.sleep(0.5)
    ai.keyDown('ctrl')
    ai.press('d')
    ai.keyUp('ctrl')
    ai.moveTo(80, 207)
    ai.click()
    msg = "กำลัง Login เกมส์เข้าสู่เซิร์ฟเวอร์"
    return msg.strip()


def goto_home():
    time.sleep(1)
    ai.moveTo(x=315, y=206)
    ai.click()
    ai.press('x')
    time.sleep(1)
    ai.press('t')
    time.sleep(1)
    ai.press('tab')
    time.sleep(1)
    ai.press('tab')
    time.sleep(1)
    ai.write("#teleport 240715.578 81483.711 0")
    time.sleep(1)
    ai.press('enter')
    time.sleep(1)
    ai.write("#ListSpawnedVehicles true")
    time.sleep(1)
    ai.press('enter')
    msg = "โดรนมาประจำตำแหน่งเริ่มต้นเรียบร้อย"
    return msg.strip()

def fixed_lost():
    time.sleep(1)
    ai.moveTo(x=315, y=206)
    ai.click()
    time.sleep(0.5)
    ai.press('esc')
    time.sleep(1)
    ai.moveTo(80, 207)
    time.sleep(0.5)
    ai.click()
    time.sleep(90)
    ai.press('x')
    time.sleep(1)
    ai.press('t')
    time.sleep(1)
    ai.press('tab')
    time.sleep(1)
    ai.press('tab')
    time.sleep(1)
    ai.write("#teleport 240715.578 81483.711 0")
    time.sleep(1)
    ai.press('enter')
    time.sleep(1)
    ai.write("#ListSpawnedVehicles true")
    time.sleep(1)
    ai.press('enter')
    msg = "กำลัง Login เข้าเซิร์ฟเวอร์อีกครั้ง"
    return msg.strip()


def cmd(txt_command):
    time.sleep(1)
    ai.moveTo(x=315, y=206)
    ai.click()
    time.sleep(0.5)
    ai.write(txt_command)
    time.sleep(0.2)
    ai.press('enter')
    msg = str(txt_command)
    return msg.strip()

# def checkout(order, steam_id):
#     while True:
#         check = check_queue()
#         if check != 0:
#             time.sleep(1)
#             data = get_pack(order)
#             spawn = data.split(',')
#             for x in spawn:
#                 time.sleep(0.5)
#                 ai.



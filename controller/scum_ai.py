import time

import pyautogui as ai
import pygetwindow as gw
import pandas as pd
import pyperclip

from database.db_config import read_db_config

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
    ai.moveTo(x=75, y=209)
    ai.click()
    msg = "กำลัง Login เกมส์เข้าสู่เซิร์ฟเวอร์อาจใช้เวลาราว 1-2 นาที"
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
    ai.moveTo(x=312, y=219)
    ai.click()
    time.sleep(1)
    ai.moveTo(x=75, y=209)
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
    msg = "กำลัง Login เข้าเซิร์ฟเวอร์อีกครั้งอาจใช้เวลาราว 1-2 นาที"
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


def get_location(location):
    time.sleep(0.5)
    ai.moveTo(x=315, y=206)
    ai.click()
    time.sleep(0.5)
    ai.write(location)
    time.sleep(0.5)
    ai.press('enter')
    time.sleep(5)
    txt = pyperclip.paste()
    msg = f'ตำแหน่งของคุณคือ {txt}'
    return msg.strip()


def listplayers():
    time.sleep(0.5)
    ai.moveTo(x=315, y=206)
    ai.click()
    time.sleep(0.5)
    ai.write('#listplayers true')
    time.sleep(0.5)
    ai.press('enter')
    time.sleep(0.5)
    txt = pyperclip.paste()
    df = pd.read_clipboard(txt)
    index = df.index
    number_of_rows = len(index) - 1
    text = df.to_string(index=False)
    msg = '```{}\n\n==================================================\n' \
          'Total {} player and 1 Drone```'.format(text, number_of_rows)
    return msg.strip()


def countplayers():
    time.sleep(0.5)
    ai.moveTo(x=315, y=206)
    ai.click()
    time.sleep(0.5)
    ai.write('#listplayers true')
    time.sleep(0.5)
    ai.press('enter')
    time.sleep(0.5)
    txt = pyperclip.paste()
    df = pd.read_clipboard(txt)
    index = df.index
    number_of_rows = len(index) - 1
    text = df.to_string(index=False)
    msg = "ขณะนี้มีผู้เล่นออนไลน์ ทั้งหมด **{}** คน บอท 1 ตัว".format(number_of_rows)
    return msg.strip()


def check_screen():
    time.sleep(2)
    ai.screenshot('check_1.png', region=(0, 0, 600, 400))

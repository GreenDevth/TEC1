import time
import pyautogui as ai
import pygetwindow as gw


def start_game():
    time.sleep(0.5)
    icon = "./img/icon.PNG"
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
    ai.moveTo(scum)
    ai.doubleClick(scum)
    msg = "กำลังเริ่มเกมส์ โปรดรอสักครู่"
    return msg.strip()


def login_game():
    time.sleep(0.5)
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
    time.sleep(0.5)
    login = "./img/login.PNG"
    scum = ai.locateOnScreen(login, grayscale=True, confidence=0.5)
    ai.moveTo(scum)
    time.sleep(1)
    ai.click(scum)
    ai.press('x')
    time.sleep(1)
    ai.press('t')
    time.sleep(1)
    ai.press('tab')
    time.sleep(1)
    ai.write('I am Home C2N1')
    time.sleep(1)
    ai.press('enter')
    time.sleep(1)
    ai.write("#teleport 240715.578 81483.711 0")
    time.sleep(1)
    ai.press('enter')
    time.sleep(1)
    msg = "กำลังส่งบอทไปยังจุดเริ่มต้น"
    return msg.strip()


def lost():
    time.sleep(0.5)
    print(ai.position())
    # lost_connect = "./img/lost.PNG"
    # scum = ai.locateOnScreen(lost_connect, grayscale=True, confidence=0.5)
    ai.moveTo(313, 215)
    ai.click()
    ai.moveTo(76, 210)
    ai.click()
    msg = "กำลังทำการ Login เข้าสู่เซิร์ฟเวอร์ใหม่อีกครั้ง"
    return msg.strip()


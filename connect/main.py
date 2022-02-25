import pyautogui as ai
import schedule
import time
import datetime

def job():
    print('hello world')
    time.sleep(1)
    login = "login.PNG"
    connect = ai.locateOnScreen(login, grayscale=True, confidence=0.9)
    ai.moveTo(connect)
    time.sleep(1)
    ai.doubleClick()
    time.sleep(1)
    ai.moveTo(1227, 495)
    time.sleep(1)
    ai.moveTo(1182, 579)
    time.sleep(1)
    ai.click()
    time.sleep(1)
    ai.click(1243, 547)

# schedule.every(5).seconds.do(job)
schedule.every().day.at("00:00").do(job)
# schedule.run_pending()
while True:
    schedule.run_pending()
    time.sleep(1)
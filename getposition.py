import pyautogui
import time

while True:
    positions = pyautogui.position()
    time.sleep(1)
    print(positions)
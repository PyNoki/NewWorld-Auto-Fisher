import pyautogui
import pydirectinput
from pyautogui import *
from pynput.keyboard import *
import random
from pynput.keyboard import Key, Controller
import time

def resetCursor2():
    time.sleep(2)
    pyautogui.keyDown('tab')
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen('1.png')
    time.sleep(0.3)
    pydirectinput.click(x, y)  
    time.sleep(1)
    pydirectinput.keyDown('esc')
    time.sleep(1)
    pydirectinput.moveRel(175, None)

def repairPole():
    time.sleep(2)
    pyautogui.keyDown('tab')
    time.sleep(2)
    a, b = pyautogui.locateCenterOnScreen('f3.png')
    time.sleep(0.3)
    pydirectinput.click(a, b)
    time.sleep(1)
    pydirectinput.moveRel(-45, None)
    time.sleep(0.5)
    pydirectinput.click()
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen('repairtext.png', confidence=0.8)
    time.sleep(1)
    pydirectinput.click(c, d)
    time.sleep(1)
    pyautogui.keyDown('e')
    time.sleep(1)
    pydirectinput.keyDown('esc')
    time.sleep(2)
    print('Pole repaired')
    time.sleep(2)






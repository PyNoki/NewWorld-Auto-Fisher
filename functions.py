import pyautogui
import pydirectinput
from pyautogui import *
from pynput.keyboard import *
import random
from pynput.keyboard import Key, Controller
import time

def resetCursor2():
    time.sleep(2)
    pydirectinput.keyDown('tab')
    pydirectinput.keyUp('tab')
    time.sleep(2)
    x, y = pyautogui.locateCenterOnScreen('1.png')
    time.sleep(0.3)
    pydirectinput.click(x, y)  
    time.sleep(1)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(1)
    pydirectinput.moveRel(175, None)

def repairPole():
    time.sleep(2)
    pydirectinput.keyDown('tab')
    pydirectinput.keyUp('tab')
    time.sleep(2)
    a, b = pyautogui.locateCenterOnScreen('f3.png')
    time.sleep(0.3)
    pydirectinput.click(a, b)
    time.sleep(1)
    pydirectinput.moveRel(-45, None)
    time.sleep(0.5)
    pydirectinput.keyDown('r')
    time.sleep(0.3)
    pydirectinput.click()
    pydirectinput.keyUp('r')
    time.sleep(1)
    pyautogui.keyDown('e')
    time.sleep(1)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(2)
    print('Pole repaired')
    time.sleep(2)






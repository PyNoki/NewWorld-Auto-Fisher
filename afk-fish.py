import pyautogui
from pyautogui import *
from pynput.keyboard import *
import random
from pynput.keyboard import Key, Controller
import time

clicktime = False
reeltime = False

while True:

    if pyautogui.locateOnScreen('waitingforcast.png') != None:
        print('waiting to cast')
        time.sleep(random.randrange(1,2))
        pyautogui.keyDown('-')
        pyautogui.keyUp('-')
        time.sleep(random.randrange(2,5))

    elif pyautogui.locateOnScreen('polecasted.png') != None:
        print('were casted')
        clicktime = True

    elif clicktime == True:
        print('Gotta click this fish')
        pyautogui.keyDown('-')
        pyautogui.keyUp('-')
        time.sleep(0.5)
        reeltime = True
        clicktime = False

    elif reeltime == True:
        print('WE FISHIN')
        pyautogui.keyDown('-')
        time.sleep(random.randrange(0,1)) #Comment this line out for larger fish and uncomment the below line
        #time.sleep(0.3) un-comment this out to catch larger fish and comment the line above ^
        pyautogui.keyUp('-')
        

from functions import *

clicktime = False
reeltime = False
standing = False
weildingRod = False

while True:

    if pyautogui.locateOnScreen('waitingforcast.png') != None:
        weildingRod = True

    if pyautogui.locateOnScreen('standing.png') != None:
        pydirectinput.keyDown('f3')
        pydirectinput.keyUp('f3')
        time.sleep(1)
        if pyautogui.locateOnScreen('poleisbrokenalert.png', confidence = 0.5) != None:
            repairPole()
            print ('pole repaired')
            time.sleep(2)
            pydirectinput.keyDown('f3')
            pydirectinput.keyUp('f3')
            time.sleep(0.2)
            standing = False

    elif pyautogui.locateOnScreen('waitingforcast.png') != None and weildingRod == True:
        print('waiting to cast')
        time.sleep(random.randrange(1,2))
        pyautogui.keyDown('-')
        pyautogui.keyUp('-')
        time.sleep(1)
        
        if pyautogui.locateOnScreen('castmissed.png', confidence = 0.8) != None:
            print('resetting cursor')
            resetCursor2()

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
        if pyautogui.locateOnScreen('hold1.png', confidence=0.7) != None:
            pyautogui.keyDown('-')
            print('Hold1')

        else:
            pyautogui.keyUp('-')
            print('Release')

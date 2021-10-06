from imports import *

keyboard = Controller()

#  ======== settings ========
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.backspace
#  ==========================

pause = True
running = True

clicktime = False
reeltime = False
standing = False
weildingRod = False
fishcaught = 1
findstatus = True
status = ''

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("Autofisher is running")
    print("- Controls:")
    print("\t f1 = Resume")
    print("\t f2 = Pause")
    print("\t backspace = Exit")
    print("-----------------------------------------------------")
    print('Press f1 to start ...')

def main():

    clicktime = False
    reeltime = False
    standing = False
    weildingRod = False
    fishcaught = 1
    findstatus = True
    status = ''
    
    #Fishing Pole EQUIPPTED in inventory coords
    x = 0
    y = 0

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            if findstatus == True:

                if fishcaught == 20:
                    time.sleep(2)
                    pydirectinput.keyDown('tab')
                    pydirectinput.keyUp('tab')
                    time.sleep(2)
                    pydirectinput.moveTo(x, y)
                    time.sleep(2)
                    pydirectinput.keyDown('r')
                    time.sleep(1)
                    pydirectinput.click()
                    pydirectinput.keyUp('r')
                    time.sleep(1)
                    pyautogui.keyDown('e')
                    pyautogui.keyUp('e')
                    time.sleep(1)
                    pydirectinput.keyDown('esc')
                    pydirectinput.keyUp('esc')
                    time.sleep(2)
                    print('Pole repaired')
                    time.sleep(2)
                    pydirectinput.keyDown('f3')
                    pydirectinput.keyUp('f3')
                    time.sleep(1)
                    fishcaught = 0

                #Step 6
                if status == 'casted':
                    if pyautogui.locateOnScreen('waitingforcast.png', confidence = 0.8) != None:
                        status = 'readytocast'

                    elif pyautogui.locateOnScreen('polecasted.png', confidence = 0.8) == None:
                        print ('Gotta click this fish')
                        pydirectinput.keyDown('-')
                        pydirectinput.keyUp('-')
                        time.sleep(0.5)
                        status = 'reeltime'

                #Step 1
                if pyautogui.locateOnScreen('standing.png') != None:
                    status = 'equiptpole'

                #Step 2
                if status == 'equiptpole':
                    pydirectinput.keyDown('f3')
                    pydirectinput.keyUp('f3')
                    time.sleep(1)
                    status = 'poleequipt'

                #Step 3
                if pyautogui.locateOnScreen('waitingforcast.png', confidence = 0.8) != None and findstatus == True:
                    status = 'readytocast'
                    print('holding the rod')

                #Step 4
                if status == 'readytocast':
                    print('casting pole')
                    time.sleep(random.randrange(1,2))
                    pydirectinput.keyDown('-')
                    pydirectinput.keyUp('-')
                    time.sleep(2)
                    status = 'waitingforbite'

                #Step 5
                if status == 'waitingforbite' and pyautogui.locateOnScreen('polecasted.png', confidence = 0.8) != None :
                    status = 'casted'
                    print('rod casted')
                    pydirectinput.keyDown('altleft')
                
            #Step 7
            if status == 'reeltime':
                print('TIME TO FIGHT THE FISH')
                status = 'tugtime'
                findstatus = False

            if status == 'tugtime':
                if pyautogui.locateOnScreen('hold1.png', confidence=0.7) != None or pyautogui.locateOnScreen('hold2.png', confidence=0.8) != None or pyautogui.locateOnScreen('hold3.png', confidence=0.9) != None or pyautogui.locateOnScreen('hold4.png', confidence=0.9) != None:
                    pydirectinput.keyDown('-')
                    print('Hold1')

                else:
                    pydirectinput.keyUp('-')
                    print('Release')

                if pyautogui.locateOnScreen('waitingforcast.png', confidence = 0.8) != None:
                    print('Grats on the fish! - Restarting loop')
                    fishcaught += 1
                    pydirectinput.keyUp('altleft')
                    findstatus = True
                    status = ''
                    

    lis.stop()

if __name__ == "__main__":
    main()
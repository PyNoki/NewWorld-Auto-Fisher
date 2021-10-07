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
fishcaught = 0
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
    release = 0
    status = ''
    
    #Fishing Pole EQUIPPED in inventory co-ords
    x = 0
    y = 0

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            if findstatus == True:

                #Step 6 (if casted - at the top for faster detection)
                if status == 'casted':
                    if pyautogui.locateOnScreen('polecasted.png', confidence = 0.8) == None:
                        print ('Gotta click this fish')
                        pydirectinput.keyDown('-')
                        pydirectinput.keyUp('-')
                        time.sleep(0.5)
                        status = 'reeltime'

                # If caught x amt of fish, repair    
                if fishcaught == 10:
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

                #Step 1 (to start the loop)
                if status == '':
                    if pyautogui.locateOnScreen('standing.png') != None:
                        status = 'equiptpole'
                        release = 0
                        print('Gotta equipt the rod')

                    if pyautogui.locateOnScreen('waitingforcast.png', confidence = 0.8) != None:
                        status = 'readytocast'
                        print('holding the rod')

                #Step 2 (equipt pole if we see the number 2)
                if status == 'equiptpole':
                    pydirectinput.keyDown('f3')
                    pydirectinput.keyUp('f3')
                    time.sleep(1)
                    status = 'readytocast'

                #Step 4 (cast the rod if we see the fishhook)
                if status == 'readytocast':
                    print('casting pole')
                    release = 0
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
                if pyautogui.locateOnScreen('hold1.png', confidence=0.7) != None or pyautogui.locateOnScreen('hold2.png', confidence=0.8) != None or pyautogui.locateOnScreen('hold3.png', confidence=0.9) != None:
                    pydirectinput.keyDown('-')
                    print('Hold1')

                    if release > 0:
                        release -= 1

                else:
                    pydirectinput.keyUp('-')
                    print('release')
                    release += 1

                    if release > 10:
                        print('Grats on the fish! (I hope) -- Restarting loop')
                        pydirectinput.keyUp('altleft')
                        fishcaught += 1
                        status = ''
                        findstatus = True          

    lis.stop()

if __name__ == "__main__":
    main()

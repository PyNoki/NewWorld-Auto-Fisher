from imports import *

keyboard = Controller()

#  ======== settings ========
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.backspace
#  ==========================

pause = True
running = True

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

    #Fishing Pole EQUIPPTED in inventory coords
    x = 0
    y = 0
    waterType = 0 #Do you want to use bait? 1 = Fresh water, 2 = Salt water (DO NOT HAVE MORE THEN 5 TYPES OF BAIT FOR SALT OR WATER)

    clicktime = False
    reeltime = False
    standing = False
    weildingRod = False
    hasBait = True
    findstatus = True
    fishcaught = 0
    release = 0
    status = ''

    #fresh positions
    freshX = x + 315 
    freshY = y - 210
    freshA = freshX + randint(-5,5)
    freshB = freshY + randint(-5,5)

    #salt position 
    saltX = x + 315
    saltY = y - 72
    saltA = saltX  + randint(-5,5)
    saltB = saltY + randint(-5,5)

    #Button position
    EquiptX = x + 628
    EquiptY = y + 150
    randomEquiptA = EquiptX + randint(-5,5)
    randomEquiptB = EquiptY + randint(-5,5)

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
                    if pyautogui.locateOnScreen('standing.png', confidence = 0.8) != None:
                        status = 'equiptpole'
                        release = 0
                        print('Gotta equipt the rod')

                    if pyautogui.locateOnScreen('f3.png', confidence = 0.8) != None:
                        status = 'checkforbait'
                        print('holding the rod')

                #Step 2 (equipt pole if we see the number 2)
                if status == 'equiptpole':
                    pydirectinput.keyDown('f3')
                    pydirectinput.keyUp('f3')
                    time.sleep(1)

                    if waterType > 0:
                        status = 'checkforbait'
                    else:
                        status = 'readytocast'

                #Check if bait is already equiped before casting
                if status == 'checkforbait':
                    if pyautogui.locateOnScreen('f3.png', confidence = 0.8) != None and pyautogui.locateOnScreen('waitingforcast.png', confidence=0.8) == None:
                        baitEquipped = True
                        status = 'readytocast'
                        print('Bait found to be equipped')
                    else:
                        baitEquipped = False
                        status = 'readytocast'

                #Step 4 (cast the rod if we see the fishhook)
                if status == 'readytocast' and waterType == 0 or hasBait == False:
                    time.sleep(3)
                    print('casting pole')
                    release = 0
                    time.sleep(random.randrange(1,2))
                    pydirectinput.keyDown('-')
                    pydirectinput.keyUp('-')
                    time.sleep(2)
                    status = 'waitingforbite'

                if status == 'readytocast' and waterType > 0 and baitEquipped == True:
                    time.sleep(3)
                    print('casting pole')
                    release = 0
                    time.sleep(random.randrange(1,2))
                    pydirectinput.keyDown('-')
                    pydirectinput.keyUp('-')
                    time.sleep(2)
                    status = 'waitingforbite'

                #if we have bait and fresh water
                if status == 'readytocast' and waterType == 1 and baitEquipped == False and hasBait == True:
                    time.sleep(2)
                    pydirectinput.keyDown('r')
                    pydirectinput.keyUp('r')
                    time.sleep(2)
                    print('putting on fresh bait')
                    pydirectinput.moveTo(freshA, freshB)
                    time.sleep(randint(1,2))
                    pydirectinput.click()
                    time.sleep(randint(1,2))
                    pydirectinput.moveTo(randomEquiptA, randomEquiptB)
                    time.sleep(randint(1,2))
                    pydirectinput.click()
                    time.sleep(randint(1,2))

                    if pyautogui.locateOnScreen('waitingforcast.png', confidence = 0.8) != None:
                        waterType = 0
                        hasBait == False
                        print('Doesnt have any fresh bait')

                    print('casting with fresh bait')
                    release = 0
                    time.sleep(random.randrange(3,4))
                    pydirectinput.keyDown('-')
                    pydirectinput.keyUp('-')
                    print('pressed - ')
                    time.sleep(2)
                    status = 'waitingforbite'

                #if we have bait and salt water
                if status == 'readytocast' and waterType == 2 and baitEquipped == False and hasBait == True:
                    time.sleep(2)
                    pydirectinput.keyDown('r')
                    pydirectinput.keyUp('r')
                    time.sleep(2)
                    print('putting on salt bait')
                    pydirectinput.moveTo(saltA, saltB)
                    time.sleep(randint(1,2))
                    pydirectinput.click()
                    time.sleep(randint(1,2))
                    pydirectinput.moveTo(randomEquiptA, randomEquiptB)
                    time.sleep(randint(1,2))
                    pydirectinput.click()
                    time.sleep(randint(1,2))

                    if pyautogui.locateOnScreen('waitingforcast.png', confidence = 0.8) != None:
                        waterType = 0
                        hasBait == False
                        print('Doesnt have any salt bait')

                    print('casting with salt bait')
                    release = 0
                    time.sleep(random.randrange(3,4))
                    pydirectinput.keyDown('-')
                    pydirectinput.keyUp('-')
                    print('pressed - ')
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

                    if release > 15:
                        print('Grats on the fish! (I hope) -- Restarting loop')
                        pydirectinput.keyUp('altleft')
                        fishcaught += 1
                        status = ''
                        findstatus = True          

    lis.stop()

if __name__ == "__main__":
    main()

import pyautogui

get1 = input('\nPlace cursor at the top left of the region you want to capture, and then press enter \n')
pos1 = pyautogui.position()

get2 = input('Now place your cursor at the bottom right of the region you want to capture, and press enter \n')
pos2 = pyautogui.position()

width = pos2[0] - pos1[0]
height = pos2[1] - pos1[1]

print('Your region is... \n')

print('region=('+str(pos1[0])+','+str(pos1[1])+','+str(width)+','+str(height)+') \n')

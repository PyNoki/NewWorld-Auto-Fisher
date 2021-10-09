# Features

- Bait support 
- Auto repair will repair every 10 catches
- Anti detection (still a work in progress) but using random times and click positions

# Prerequisites

- pip install pyautogui
- pip install pydirectinput
- pip install pynput
- pip install pillow
- pip install opencv-python

# Setup

- 1920 x 1080 resolution Full screen (windowed is untested)
- You MUST run getposition.py and put your cursor in the middle of the fishing rod while its equipped to your character (the console will tell you your current mouse position). THEN inside of run.py insert your X position on line 39 and Y position on line 40.

# Keybinds

- Your fishing cast key must be '-'
- Your inventory key must be 'tab' (default)
- Your freelook key must be 'left alt' (default)
- Your repair must be 'r' (default)

# Using bait

- The bot will use all the bait you have by default, if you don't want it to use any bait then go to line 41 and change it to "waterType = 0" 

# About to start

- Position yourself so that you're not too deep in the water, and that you can still open your inventory
- Make sure your cast will land in the water with the bare minimum cast
- Make sure your crosshair is in a good position

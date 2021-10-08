# Features

- Bait support 
- Auto repair will repair every 10 catches
- Anti detection (still a work in progress) but using random times and click positions

# Prerequisites

--pip install pyautogui

--pip install pydirectinput

# Setup

- 1920 x 1080 resolution Full screen (windowed is untested)
- You MUST run getposition.py and put your cursor in the middle of the fishing rod while its equipped to your character (the console will tell you your current mouse position). THEN inside of run.py insert your X position on line 39 and Y position on line 40.
- FOR USING BAIT You MUST edit line 41 and change "waterType" to be " = 1 " for fresh water or " = 2 " for salt water (leave it at 0 if you don't want to use bait)

# Keybinds

- Your fishing cast key must be '-'
- Your inventory key must be 'tab' (default)
- Your freelook key must be 'left alt' (default)
- Your repair must be 'r' (default)

# Using bait

- Do not have more then 5 slots of bait for a water type, so don't have 6 or 7 types of fresh water bait in your inventory, max 5. Same goes for salt water.

# About to start

- Position yourself so that you're not too deep in the water, and that you can still open your inventory
- Make sure your cast will land in the water with the bare minimum cast
- Make sure your crosshair is in a good position

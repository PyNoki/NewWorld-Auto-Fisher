• Change your fishing cast key to "-"
• DO NOT stand in the water while fishing, or else the bot can't fix your pole
• PUT UR SETTINGS ON HIGH

--Packages you will need--
pip install pynput
pip install PyAutoGUI
pip install opencv-python
pip install PyDirectInput

ALSO - If you have problems with the images not being detected, its because they arent a pixel perfect match, this includes

1 - waitingforcast.png
2 - standing.png
3 - polecasted.png
4 - 1.png
5 - f3.png

The rest of the images are using confidence from OpenCV so it should detect those almost every time.

So please look at the images and take your own if needed ()

If you needed to install more or ran into problems please let me know

https://github.com/PyMan142/NewWorld-Auto-Fisher

----------------------

Changes from v1 - v2 are the following

New Packages added
• pip install PyDirectInput
• pip install opencv-python

• Detection for pole breaking & fixing
• Detection for cast not landing in the water (this happened after you catch a tier 3 or higher fish)
• Moving mouse when cast wasn't in the water
• Using OpenCV for tug of war with the fish, this results in much faster speeds and usually gets bigger fish! 

I am still working on adding bait, but I managed to pull this together pretty fast. 
Thank you for your feedback as always.

"""
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 683,479
"""

import ImageGrab
import os
import time

# Globals
# ------------------
 
x_pad = 800
y_pad = 800

def screenGrab():
	box = (x_pad+1,y_pad+1,683,479)
	im = ImageGrab.grab()
	im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png')

def main():
	screenGrab()
	
if __name__=='__main__':
	main()
"""
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 683,479
"""
import win32api,win32con
import ImageGrab
import os
import time

# Globals
# ------------------
 
x_pad = 800
y_pad = 800

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) 
	print "Click." #completely optional, just for debugging
	
def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	print 'left down'
	
def leftUp():
	Wwin32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(.1)
	print 'left release'
	
def mousePos(cord):
	win32api.SetCursorPos((x_pad + cord[0],y_pad + cord[1])
	
def get_cords():
	x,y = win32api.GetCursorPos()
	x=x - x_pad
	y=y - y_pad
	print x,y
	
def screenGrab():
	box = (x_pad+1,y_pad+1,683,479)
	im = ImageGrab.grab()
	im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png')

def main():
	screenGrab()
	
if __name__=='__main__':
	main()
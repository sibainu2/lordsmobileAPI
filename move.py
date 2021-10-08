from __future__ import division
import pyautogui
from time import sleep
import screenshot


def move(i):#1タイル横約211.5縦107.3
    screenshot.screenshot(i)
    pyautogui.moveTo(1200,500)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(160,500,1)
    pyautogui.mouseUp(button='left')


sleep(3)

move()


#pos = pyautogui.position()
#print(pos)
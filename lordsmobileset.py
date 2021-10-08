from time import sleep
import win32gui

meveapp = win32gui.FindWindow(None,"Discord(32ビット)")
#sleep(1)
#win32gui.SetForegroundWindow(meveapp)

sleep(1)

hwnd =win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd,0,0,500,500,True)
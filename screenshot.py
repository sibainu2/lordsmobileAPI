import pyautogui

from time import sleep
sleep(3)

def screenshot(i):
    #スクリーンを撮る
    screenshot1 = pyautogui.screenshot(region = (105, 240, 1080, 778))#1170
    screenshot1.save(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\Photo\map_"+str(i)+"_1.png")#保存先
    screenshot2 = pyautogui.screenshot(region = (105, 240, 1080, 778))#1170
    screenshot2.save(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\Photo\map_"+str(i)+"_2.png")#バリア用
    
    
screenshot(i=1)
#pyautogui.moveTo(x=106, y=234)
#pos = pyautogui.position()
#print(pos)
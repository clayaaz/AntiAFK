import pyautogui, time, random

time.sleep(4)
i = True

while i:
    ranNum = random.randint(a=0, b=3)

    if ranNum == 0:
        pyautogui.press('w')
    elif ranNum == 1:
        pyautogui.press('a')    
    elif ranNum == 2:
        pyautogui.press('s')
    elif ranNum == 3:
        pyautogui.press('d')

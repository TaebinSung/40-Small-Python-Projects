import pyautogui
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pic1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic4.png')
    print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

# pyperclip.copy("This is an automated message~~")
pyautogui.write("This is an automated message~~")
time.sleep(1.0)
pyautogui.write(["enter"])
time.sleep(1.0)
pyautogui.write(["escape"])
time.sleep(1.0)


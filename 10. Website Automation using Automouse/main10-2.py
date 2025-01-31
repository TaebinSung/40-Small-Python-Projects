import pyautogui
import pyperclip
import time
from PIL import ImageGrab


pyautogui.moveTo(680, 195, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 400 
start_y = 265
end_x = 1070
end_y = 990
time.sleep(2)
pyautogui.screenshot("test.png")
pyautogui.screenshot(r"10. Website Automation using Automouse\weather.png", region=(start_x, start_y, end_x-start_x, end_y-start_y))

print("File saved")
    # 2315, 265
    # 2990, 990
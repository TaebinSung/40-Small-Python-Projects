import pyautogui
import time
import pyperclip

weathers = ["서울 날씨", "시흥 날씨","청주 날씨", "부산 날씨", "강원도 날씨"]

addr_x=968 
addr_y=59
start_x = 400 
start_y = 265
end_x = 1070
end_y = 990

for weather in weathers:
    pyautogui.moveTo(680, 195, 0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyperclip.copy(weather)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)   
    time.sleep(2)

    pyautogui.screenshot("test.png")
    pyautogui.screenshot(fr"10. Website Automation using Automouse\{weather}.png", region=(start_x, start_y, end_x-start_x, end_y-start_y))

    print("File saved")







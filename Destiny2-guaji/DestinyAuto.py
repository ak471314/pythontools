import sys
#导入 用于自动化控制鼠标与键盘
import pyautogui
# 用于时间处理
import time

print('Press Ctrl-C to quit.')
try:
    while True:
        #pyautogui.click(button='left',interval=1) 
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.mouseUp(button='left')
        time.sleep(0.1)
        pyautogui.keyDown('s')
        time.s(0.1)
        pyautogui.keyUp('s')
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        #pyautogui.press('s',interval=0.1)
        time.sleep(0.1)
        #pyautogui.press('ctrl',interval=0.1)
except KeyboardInterrupt:
    print('\n')
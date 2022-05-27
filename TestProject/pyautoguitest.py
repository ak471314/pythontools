#! python3
import pyautogui, sys,time
print('Press Ctrl-C to quit.')
try:
    while True:
        pyautogui.mouseDown(button='left')
        time.sleep(4)
        pyautogui.mouseUp(button='left')
        #time.sleep(0.1)
        #pyautogui.keyDown('f')
        #time.sleep(3)
        #pyautogui.keyUp('f')
except KeyboardInterrupt:
    print('\n')
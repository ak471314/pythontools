#! python3
import pyautogui, sys,time,os

print('Press Ctrl-C to quit.')

run_path=os.path.dirname(os.path.realpath(__file__))
img_path=run_path + '\img'
print("运行路径",img_path)
name = "xuanxiang"
img_name=os.path.join(img_path,name+".png")
print("图片路径",img_name)

try:
    while True:
        img_point = pyautogui.locateCenterOnScreen(img_name)
        print(img_point)
except KeyboardInterrupt:
    print('\n')
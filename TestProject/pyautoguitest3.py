#! python3
import pyautogui, sys,time,os

print('Press Ctrl-C to quit.')

run_path=os.path.dirname(os.path.realpath(__file__))
img_path=run_path + '\img'
print("运行路径",img_path)
name = "xuanxiang"
img_name=os.path.join(img_path,name+".png")
print("图片路径",img_name)
size=pyautogui.size()
print(size.width/2)
print(size.height/2)
xunhuancishu = 1
print(xunhuancishu)
xunhuancishu = xunhuancishu + 1
print(xunhuancishu)


def test():
    xunhuancishu = xunhuancishu + 1
    print(xunhuancishu)
    
test()

try:
    while True:
        img_point = pyautogui.locateCenterOnScreen(img_name)
        print(img_point)

        if img_point == None :
            print("aa")
        
        if img_point != None :
            print("bb")

except KeyboardInterrupt:
    print('\n')
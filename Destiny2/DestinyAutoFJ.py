#! python3
import pyautogui, sys,time,os

print('Press Ctrl-C to quit.')

run_path=os.path.dirname(os.path.realpath(__file__))
img_path=run_path + '\img'
print("运行路径",img_path)
img_name=os.path.join(img_path,"xuanxiang.png")
print("图片路径",img_name)

#定义鼠标操作方法
def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry == 1:
        while True:
            #获取应用程序位置
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                # interval 单击之间等待的秒数
                #x,y是鼠标坐标，
                #duration为执行此次动作的设置时间，0为立即执行
                #button有几个默认选项，left,middle,right,primary,secondary 默认为左键模式，后两者组合就是拖动
                #拖动语句：
                # pyautogui.dragTo(x=None, y=None, duration=0.0, button='primary', mouseDownUp=True)
                # mouseDownUp设置为False则鼠标只是单纯的移动，不会按下与松开 duration设置为0或不设置也不行
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
    elif reTry == -1:
        while True:
            # confidence 查找图片精确度，默认为 1
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)

#查找图片
def findImage(imgname):
    run_path=os.path.dirname(os.path.realpath(__file__))
    img_path=run_path + '\img'
    img_name=os.path.join(img_path,imgname+".png")
    img_point = pyautogui.locateCenterOnScreen(img_name)
    return img_point


try:
    while True:
        img_point = pyautogui.locateCenterOnScreen(img_name)
        print(img_point)
except KeyboardInterrupt:
    print('\n')
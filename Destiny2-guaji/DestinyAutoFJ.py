#! python3
import pyautogui, sys,time,os

print('Press Ctrl-C to quit.')
#1366*768  低

run_path=os.path.dirname(os.path.realpath(__file__))
img_path=run_path + '\img'
print("图片路径",img_path)

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
    img_name=os.path.join(img_path,imgname+".png")
    img_point = pyautogui.locateCenterOnScreen(img_name)
    if img_point is not None:
        return True

    return False
#点击图片
def clickImgae(imgname):
    img_name=os.path.join(img_path,imgname+".png")
    mouseClick(1,"left",img_name,3)
        
#分解装备
def fenjieEquip():
    pyautogui.keyDown('f')
    time.sleep(2)
    pyautogui.keyUp('f')

#获取装备
def getEquip():
    pyautogui.mouseDown(button='left')
    time.sleep(4)
    pyautogui.mouseUp(button='left')

#角色界面
def jueseSence():
    if findImage("juesejiemian") == False:
        return
    #定位第一件

    # 分解装备
    for i in range(5):
        # 分解蓝色装备
        for i in range(10):
            fenjieEquip()

        #移动下一位
        pyautogui.move(100, 0)
        #
        pyautogui.move(100, 0)

    #进入装备
    #点击收藏
    clickImgae("jaosecandan")
    time.sleep(2)
    #点击服饰
    clickImgae("jaosecandan")
    time.sleep(2)
    #点击升级
    clickImgae("jaosecandan")
    time.sleep(2)
    #点击
    clickImgae("jaosecandan")
    time.sleep(2)

#收藏界面
def shoucangSence():
    if findImage("shoucang") == False:
        return

    #定位第一件装备

    # 获取装备
    for i in range(5):
        # 获取蓝色装备
        for i in range(20):
            getEquip()
            if findImage("kongjianbuzu"):
                break

        if findImage("kongjianbuzu"):
            #移动下一位
            pyautogui.move(100, 0)

    #返回角色
    pyautogui.press('esc')
    time.sleep(3)
    #点击角色
    clickImgae("jaosecandan")
    time.sleep(2)
    



try:
    while True:
        jueseSence()
        shoucangSence()

except KeyboardInterrupt:
    print('\n')
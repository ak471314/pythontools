#! python3
import pyautogui, sys,time,os

print('Press Ctrl-C to quit.')
#1366*768  低

run_path=os.path.dirname(os.path.realpath(__file__))
img_path=run_path + '\img'
print("图片路径",img_path)

equip_count = 9
xunhuancishu = 1

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
    location = pyautogui.locateCenterOnScreen(img_name)
    if location is not None:
        return True

    return False
#点击图片
def clickImgae(imgname,clickTimes=1):
    print("find lickImgae : ",imgname)
    img_name=os.path.join(img_path,imgname+".png")
    location = pyautogui.locateCenterOnScreen(img_name,confidence=0.8)
    if location is not None:
        for i in range(clickTimes):
            pyautogui.moveTo(location.x,location.y)
            pyautogui.click(location.x,location.y,button="left")
            print("clickImgae : ",imgname)

        time.sleep(0.5)      
    #mouseClick(1,"left",img_name,1)
    
        
#分解装备
def fenjieEquip():
    pyautogui.keyDown('f')
    time.sleep(1.6)
    pyautogui.keyUp('f')

#获取装备
def getEquip():
    pyautogui.mouseDown(button='left')
    time.sleep(3.2)
    pyautogui.mouseUp(button='left')

#角色界面
def jueseSence():
    if findImage("juese-liang") == False:
        return
    #定位第一件
    if findImage("zhuangbeitou"):
        clickImgae("zhuangbeitou")
        time.sleep(2)
        pyautogui.move(90, 0)

    # 分解装备
    for i in range(5):
        # 分解蓝色装备
        for i in range(equip_count):
            fenjieEquip()
            print("分解装备：",i)

        #移动下一位
        pyautogui.move(-90, 90)
        pyautogui.move(90, 0)

    #进入装备
    #点击收藏f
    clickImgae("shoucangpin")
    time.sleep(1)
    #点击服饰
    clickImgae("hujia")
    time.sleep(1)
    clickImgae("jibie")
    time.sleep(1)
    clickImgae("youjiantou")

#收藏界面
def shoucangSence():
    if findImage("shoucang-hujia") == False:
        return

    #定位第一件装备
    if findImage("lanzhuangtou"):
        clickImgae("lanzhuangtou")

    # 获取装备
    for i in range(5):
        # 获取蓝色装备
        for i in range(equip_count):
            getEquip()
            print("获取蓝色装备",i)
            
        #移动下一位
        pyautogui.move(75, 0)

    #返回角色
    pyautogui.press('esc')
    time.sleep(2)
    #点击角色
    clickImgae("juese")
    time.sleep(1)
    size=pyautogui.size()
    pyautogui.moveTo(size.width/2,size.height/2)

    global xunhuancishu
    xunhuancishu = xunhuancishu + 1

def duihuan():
    #兑换
    if findImage("shuzhi") == False:
        return
    print("兑换")
    #定位树脂
    clickImgae("shuzhi")
    for i in range(40):
        pyautogui.click(button="left")
        time.sleep(1)
    
    pyautogui.move(-200, 0)
    for i in range(10):
        pyautogui.click(button="left")
        time.sleep(1)
    
    pyautogui.press('f1')
    time.sleep(1)

    global xunhuancishu
    xunhuancishu = 1

#买微光
def buyWei():
    pyautogui.press('f1')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.keyDown('e')
    time.sleep(2)
    pyautogui.keyUp('e')
    time.sleep(5)
    
    duihuan()

try:
    while True:
        if xunhuancishu < 6 :
            jueseSence()
            shoucangSence()
            duihuan()
        else:
            buyWei()

except KeyboardInterrupt:
    print('\n')
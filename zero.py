"""
import hashlib

string = "123456"

m = hashlib.md5()       # 创建md5对象
str_bytes = string.encode(encoding='utf-8')
print(type(str_bytes))
m.update(str_bytes)   # update方法只接收bytes类型数据作为参数
str_md5 = m.hexdigest()     # 得到散列后的字符串

print('MD5散列前为 ：' + string)
print('MD5散列后为 ：' + str_md5)

def add(x: int, y: int)->int:
    return x + y


print(add(3, 4.3))



class PositiveInteger(int):
    def __init__(self, value):
        print(type(self), self)
        super(PositiveInteger, self).__init__()

i = PositiveInteger(-5)
print(i)

class A:
    def __init__(self):
        self.attr_a = 1
        print('执行A的初始化函数')


class B(A):
    def __init__(self):
        A.__init__(self)
        self.attr_b = 2

b = B()
print(b.attr_a, b.attr_b)


import os
import linecache
a=os.popen('adb shell dumpsys bluetooth_manager')
b=a.readlines()
lines=[]
for line in b:
    if 'Connections' in line:
        lines.append(line)
num=b.index(lines[0])
bluetooth=b[num+1].split()[5]
print(bluetooth)



from element.bluetooth_page import Bluetooth_Page as BLUETOOTH
from operate.operate_packaging import operate_packaging
from common.element_operate import element_operate
from element.mian_page import Main_Page as MAIN
from common.start_app import start_app
from common.logger import logger
from common.public import level_
from time import sleep
import pytest
import allure
from threading import Thread
import threading

driver=start_app()
lock = threading.Lock()

def test_connect_bluetooth():
    lock.acquire()
    operate_packaging(driver).bluetooth_connect()
    lock.release()
    is_success = element_operate.is_exist_element(driver=driver, loc=MAIN.bluetooth_sign, info='MAIN')
    assert is_success
    element_operate(driver).click_element(loc=MAIN.bluetooth_sign, info='MAIN')
    element_operate(driver).press_element(loc=BLUETOOTH.bluetooth_number, info='BLUETOOTH')
    sleep(3)


def bluetooth_abnormal():
    try:
        WebDriverWait(driver, 500, 3).until(lambda x: x.find_element(*MAIN.bluetooth_abnormal))
    except Exception:
        pass
    else:
        logger.error('APP蓝牙异常断开')


import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


import sys

def a(count):
    b(count - 1)
    print(count)

def b(count):
    c(count - 1)
    print(count)

def c(count):
    c_frame = sys._getframe()       # 函数c的frame
    print(c_frame.f_code, c_frame.f_lineno, c_frame.f_locals)

    b_frame = c_frame.f_back        # 函数b的frame
    print(b_frame.f_code, b_frame.f_lineno, b_frame.f_locals)

    a_frame = b_frame.f_back        # 函数a的frame
    print(a_frame.f_code, a_frame.f_lineno, a_frame.f_locals)
    print(count)

a(3)


#WIFI连接控制手机
import os
os.popen('adb tcpip 5555')
os.popen('adb connect 192.168.137.248:5555')



import time
class Screen():
    def __init__(self,name):
        self.name=name

    def __call__(self):
        nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
        time_name = self.name + '=' + nowTime
        print(time_name)


p=Screen(name='dad')
p()



x=lambda info:list(filter(None,info.split(' '))) if info else []
y=x('fas ada da ')
print(y)


import time
test_case='test_try.py'
report_name=str(test_case).split('.')[0]+'-'+time.strftime('%Y-%m-%d')
print(report_name)


path='C:/Users/lisijie/PycharmProjects/起爆器APP测试/data/test_data.xlsx'
report_name=path.split('/')[-1:]
print(report_name)




# 编写钩子函数
#失败用例自动截图函数
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        print('用例失败...')  #调用截图函数


driver = None


#  module confest
# 初始化用例
@pytest.fixture(scope='module', autouse=False)
def Sys_user_manage_page():
    print('初始化用例')
    global driver
    if driver is None:
        driver = Sys_user_manage('Chrome')
        driver.login('superadmin', '123456')
    yield driver
    print('结束用例')
    driver.close_Browser()
    driver = None


# confest.py中定义截图函数
def _fail_picture():
    driver.fail_picture()


# 编写钩子函数
# 失败用例自动截图函数
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        _fail_picture()  # 调用截图函数


from element.bluetooth_page import Bluetooth_Page as Bluetooth
from element.main_page import Main_Page as Main
from common.start_app import start_app
from common.element_operate import element_operate
from selenium.webdriver.common.by import By
from time import sleep

def swipe_element():
    driver=start_app()
    app=element_operate(driver)

    app.click_element(loc=Main.bluetooth_sign,info='')
    app.click_element(loc=Bluetooth.bluetooth_number,info='')
    app.get_element_toast(loc=Bluetooth.bluetooth_connect_success,info='')
    app.click_element(loc=Main.register,info='')
    for i  in range(0,20):
        app.swipe_element(start_location=[240,702],end_location=[240,417],info='')
        sleep(0.5)

    sleep(5)
    app.return_button(current_info='',return_info='')
    comfirm_button=(By.ID,'prod.prod:id/md_button_positive')
    #comfirm_button=(By.XPATH, '//*[@text=\'{}\']'.format('确定'))
    app.click_element(loc=comfirm_button,info='')


swipe_element()





x=['  Connections: 1\n', '  mMaxHeadsetConnections: 1\n', '  DefaultMaxHeadsetConnections: 1\n']
if len(x)==3:
    print('正确')



from common.read_file import read_excel
from config.file_path import data_path

x=read_excel(path=f'{data_path}/LG.xlsx',line_num=1)
print(x[1])

"""

from common.element_operate import element_operate
from common.start_app import start_app
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

driver = start_app()
app = element_operate(driver)
action = TouchAction(driver)
actions=ActionChains(driver)

class My_TouchAction(TouchAction):

    def my_release(self,element):

        while True:
            try:
                d=driver.find_element(*element)
                if len(d)==1:
                    self._add_action('release', {})
                    return self
            except Exception:
                self.wait(500)
            else:
                break


    def my_press(self,x,y):
        return self.press(x=x,y=y)

    def my_move_to(self,x,y):
        return self.move_to(x=x,y=y)

    def my_perform(self):
        return self.perform()

    def my_wait(self,ms):
        return self.wait(ms)



class Scroll(object):


    def whether_bottom(self,x1,x2):
        app.click_element(loc=(By.XPATH,'//*[@text=\'{}\']'.format('① 注册')),info='')
        sleep(3)
        while True:
            data=self.whether_isexit(x1)
            if data is True:
                print('已找到要移动的数据')
                break
            app.swipe_element(start_location=[300,700],end_location=[300,300],info='')
            data = self.whether_isexit(x1)
            if data is True:
                print('已找到要移动的数据')
                break
            data1=driver.find_elements(By.ID,'com.fhl.ed.initiator3:id/member_item_surface_code')[0].text
            app.swipe_element(start_location=[300, 700], end_location=[300, 300], info='')
            data2=driver.find_elements(By.ID,'com.fhl.ed.initiator3:id/member_item_surface_code')[0].text
            if data1==data2:
                print('已滑到列表底部')

        try:
            data = self.whether_isexit(x1)
            if data is True:
                pass
        except Exception:
            print('要移动的数据不存在')


        if self.whether_isexit(x2) is True:
            d1=driver.find_element(By.XPATH,'//*[@text=\'{}\']'.format(x1))
            d2=driver.find_element(By.XPATH,'//*[@text=\'{}\']'.format(x2))
            if d1.location['y']<560 and d2.location['y']<560:
                action.press(x=30,y=d1.location['y']+34).wait(1000).move_to(x=30,y=d2.location['y']-34).release().perform()
                print(1)
            elif d1.location['y']>560 and d2.location['y']>560:
                app.swipe_element(start_location=[300, 700], end_location=[300, 350], info='')
                sleep(2)
                d3 = driver.find_element(By.XPATH, '//*[@text=\'{}\']'.format(x1))
                d4 = driver.find_element(By.XPATH, '//*[@text=\'{}\']'.format(x2))
                action.press(x=30, y=d3.location['y'] + 34).wait(1000).move_to(x=30, y=d4.location['y'] - 34).release().perform()
                print(2)
            elif d1.location['y']<560 and d2.location['y']>560:
                action.press(x=30,y=d1.location['y']+34).wait(1000).move_to(x=30,y=
                (driver.find_element(By.XPATH, '//*[@text=\'{}\']'.format(x2))).location['y']-34).release().perform()
                #(driver.find_element(By.XPATH, '//*[@text=\'{}\']'.format(x2))).location['y']-34
                print(3)
            elif d1.location['y']>560 and d2.location['y']<560:
                action.press(x=30, y=d1.location['y'] + 34).wait(1000).move_to(x=30, y=
                (driver.find_element(By.XPATH, '//*[@text=\'{}\']'.format(x2))).location['y']+68+34).release().perform()
                print(4)
            else:
                print('出现未知错误')
        else:
            d5 = driver.find_element(By.XPATH, '//*[@text=\'{}\']'.format(x1))
            action.press(x=30,y=d5.location['y']+34).wait(1000).move_to(x=30,y=580).perform()



    def whether_isexit(self,element):
        d=driver.find_elements(By.XPATH,'//*[@text=\'{}\']'.format(element))
        if len(d)==1:
            return True
        if len(d)==0:
            return False


    def find_data(self,x1,x2):
        app.click_element(loc=(By.XPATH, '//*[@text=\'{}\']'.format('① 注册')), info='')
        sleep(3)
        d1=driver.find_element(By.XPATH,'//*[@text=\'{}\']'.format(x1))
        #d2=driver.find_element(By.XPATH,'//*[@text=\'{}\']'.format(x2))
        #action.press(x=30,y=d1.location['y']+34).wait(1000).move_to(x=30,y=480).My_TouchAction(driver).my_release(element=x2).perform()
        My_TouchAction(driver).my_press(x=30,y=d1.location['y']+34).my_wait(1000).my_move_to(x=30,y=580).my_release(element=(By.XPATH,'//*[@text=\'{}\']'.format(x2))).my_perform()


    def release_element(self,element):
        if self.whether_isexit(element) is True:
            action.release()
        else:
            action.wait()

if __name__=='__main__':
    Scroll().find_data(x1='2021031200001',x2='2021031200002')
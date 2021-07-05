from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.public import get_func_name
from user import Whether_save_recording
from common.start_app import start_app
from user import Whether_screenshot
from common.logger import logger
from config.file_path import *
import base64
import allure
import time



class element_operate(object):

    def __init__(self,driver):
        self.driver = driver


    def get_element(self,loc,info):
        """
        获取页面元素
        :param loc: 元素
        :param info: 所在页面
        :return: 获取元素
        """
        try:
            element=self.driver.find_element(*loc)
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}未找到，原因是{e}')
        else:
            return element



    def wait_element(self,loc,info,timeout=5):
        """
        等待页面元素加载
        :param loc: 元素
        :param info: 所在页面
        :param timeout: 超时时间
        :return:
        """
        try:
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}等待失败，原因是{e}')
            raise e
        else:
            pass



    def click_element(self,loc,info,timeout=5):
        """
        页面元素点击操作
        :param loc: 元素
        :param info: 所在页面
        :param timeout: 超时时间
        :return:
        """
        try:
            self.wait_element(loc,info,timeout)
            self.get_element(loc, info).click()
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}点击失败，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]} 页面的元素{loc}--点击')




    def input_element(self,loc,info,msg,timeout=25):
        """
        页面元素输入信息操作
        :param loc: 元素
        :param info: 所在页面
        :param msg: 输入内容
        :param timeout: 超时时间
        :return:
        """
        try:
            self.wait_element(loc,info,timeout)
            self.get_element(loc,info).clear()
            self.get_element(loc,info).send_keys(msg)
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}输入{msg}失败，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]} 页面的元素{loc}--输入{msg}')




    def get_element_text(self,loc,info,timeout=5):
        """
        获取元素文本信息操作
        :param loc: 元素
        :param info: 所在页面
        :param timeout: 超时时间
        :return: 元素对应的文本信息
        """
        try:
            self.wait_element(loc,info,timeout)
            data=self.driver.find_element(*loc).text
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}文本获取失败，原因是{e}')
            raise e
        else:
            return data



    def get_element_toast(self,loc,info):
        """
        获取toast信息操作
        :param loc: 元素
        :param info: 所在页面
        :return:
        """
        try:
            WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*loc))
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}找不到，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]} 页面的toast信息{loc}成功找到！')



    def is_exist_element(self,loc,info,timeout=5):
        """
        判断元素是否存在
        :param driver: driver
        :param loc: 元素
        :param info: 所在页面
        :return: bool
        """
        element = WebDriverWait(self.driver,timeout ,0.5).until(lambda x: x.find_elements(*loc))
        if len(element) == 0:
            logger.info(f'{[info]} 页面的元素{loc}不存在,判断失败！！！')
            return False
        if len(element) == 1:
            logger.info(f'{[info]} 页面的元素{loc}存在，判断成功！！！')
            return True


    @property
    def get_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y



    def tap_element(self,info,location,duration=100):
       """
       按坐标点击元素操作
       :param info: 所在页面
       :param location: 格式：[(x1,y1),(x2,y2)]
       :param duration: 持续时间
       :return:
       """
       try:
           self.driver.tap(location,duration=duration)
       except Exception as e:
           logger.error(f'{[info]} 页面的坐标{location}点击失败，原因是{e}')
           raise e
       else:
           logger.info(f'{[info]} 页面的坐标{location}点击成功')



    def swipe_element(self,info,start_location,end_location,duration=1000):
        """
        按坐标元素滑动操作
        :param info: 所在页面
        :param start_location: 格式:[x1,y1]
        :param end_location: 格式:[x1,y1]
        :param duration: 持续时间
        :return:
        """
        try:
            size = self.get_size
            x1=start_location[0]
            y1=start_location[1]
            x2=end_location[0]
            y2=end_location[1]

            if 0<x1<size[0] and 0<x2<size[0] and 0<y1<size[1] and 0<y2<size[1]:
                if x1 == x2 and y1 == y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 起始坐标和终止坐标相同，无法做滑动操作')
                elif x1 < x2 and y1 == y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向右滑动：{start_location}--->{end_location}')
                elif x1 > x2 and y1 == y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向左滑动：{start_location}--->{end_location}')
                elif x1 == x2 and y1 < y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向下滑动：{start_location}--->{end_location}')
                elif x1 == x2 and y1 > y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向上滑动：{start_location}--->{end_location}')
                elif x1 < x2 and y1 < y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向右下方滑动：{start_location}--->{end_location}')
                elif x1 < x2 and y1 > y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向右上方滑动：{start_location}--->{end_location}')
                elif x1 > x2 and y1 < y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向左下方滑动：{start_location}--->{end_location}')
                elif x1 > x2 and y1 > y2:
                    self.driver.swipe(x1, y1, x2, y2, duration=duration)
                    logger.info(f'{[info]} 向右上方滑动：{start_location}--->{end_location}')
            else:
                logger.error(f'{[info]} 滑动坐标输入超过范围，滑动失败！！！')
        except Exception as e:
            logger.error(f'{[get_func_name()]}在{info}下滑动元素{start_location}-->{end_location}发生异常错误，原因是{e}')
            raise e




    def press_element(self,info,loc,duration=1000):
        """
        元素长按操作
        :param info: 所在页面
        :param loc: 元素
        :param duration: 持续时间
        :return:
        """
        try:
            action=TouchAction(self.driver)
            element=self.get_element(info=info,loc=loc)
            action.long_press(element).wait(duration).perform()
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{loc}--长按失败，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]} 页面的元素{loc}--长按')



    def drag_and_drap(self,info,start_loc,end_loc):
        """
        元素拖拽
        :param info: 所属页面
        :param start_loc: 起始位置元素
        :param end_loc: 终止位置元素
        :return:
        """
        try:
            action = ActionChains(self.driver)
            action.drag_and_drop(start_loc, end_loc)
        except Exception as e:
            logger.error(f'{[info]} 页面的元素{start_loc}--拖拽-->{end_loc}失败，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]} 页面的元素{start_loc}--拖拽-->{end_loc}')


    #
    def screen_shot(self,info):
        """
        失败截图
        :param info: 所在页面
        :return:
        """
        try:
            info_path=picture_file+'/'+info+'/'
            rq=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
            screenshot_name=info+'-'+rq+'.png'
            screenshot_path=info_path+screenshot_name
            if Whether_screenshot==True:
                try:
                    self.driver.get_screenshot_as_file(screenshot_path)
                    allure.attach.file(
                        source=screenshot_path,name='失败截图',attachment_type=allure.attachment_type.PNG)
                    logger.info(f'{[info]} 页面的截图成功，图片名：{screenshot_name}')
                except Exception as e:
                    logger.error(f'{[info]} 页面的截图失败，原因是{e}')
                    raise e
            else:
                pass
        except Exception as e:
            logger.error(f'{[get_func_name()]}在{info}下截图时发生异常错误，原因是{e}')
            raise e


    """
    def screen_shot_another(self,info):
        try:
            info_path=picture_file+'/'+info+'/'
            rq=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
            screenshot_name=info+'-'+rq+'.png'
            screenshot_path=info_path+screenshot_name
            try:
                self.driver.get_screenshot_as_file(screenshot_path)
                allure.attach.file(
                    source=screenshot_path, name='失败截图', attachment_type=allure.attachment_type.PNG)
                logger.info(f'{[info]} 页面的截图成功，图片名：{screenshot_name}')
            except Exception as e:
                logger.error(f'{[info]} 页面的截图失败，原因是{e}')
                raise e
        except Exception as e:
            logger.error(f'{[get_func_name()]}在{info}下截图时发生异常错误，原因是{e}')
            raise e
        """




    def return_button(self,current_info,return_info):
        """
        返回按键
        :param current_info: 当前所在页面
        :param return_info: 返回后所在页面
        :return:
        """
        try:
            self.driver.press_keycode(4)
            time.sleep(1)
        except Exception as e:
            logger.error(f'{[get_func_name()]}在页面{current_info}返回到页面{return_info}时发生异常错误，原因是{e}')
            raise e
        else:
            logger.info(f'{[current_info]}=====>{[return_info]}')



    def home_button(self,info):
        """
        home键
        :param current_info: 所在页面
        :return:
        """
        try:
            self.driver.press_keycode(3)
        except Exception as e:
            logger.error(f'{[get_func_name()]}在页面{info}按下HOME键时异常错误，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]}=======>[HOME]')



    def menu_button(self,info):
        """
        菜单键
        :param info: 所在页面
        :return:
        """
        try:
            time.sleep(2)
            self.driver.press_keycode(82)
        except Exception as e:
            logger.error(f'{[get_func_name()]}在页面{info}按下菜单键时发生异常错误，原因是{e}')
            raise e
        else:
            logger.info(f'{[info]}========>[菜单键]')



    def start_recording_screen(self,case_name):
        """
        开始录屏
        :param case_name: 用例名
        :return:
        """
        try:
            self.driver.start_recording_screen(forcedRestart=True)
        except Exception as e:
            logger.error(f'{[case_name]}开始屏幕录制失败，原因是{e}')
            raise e
        else:
            logger.info(f'{[case_name]}开始屏幕录制！！！')

    #
    def stop_recording_screen(self,case_name):
        """
        停止录屏
        :param case_name: 用例名
        :return:
        """
        try:
            rq = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
            recording_name = rq + '-' + case_name + '.mp4'
            recording_path=recording_file+'/'+recording_name
            data=self.driver.stop_recording_screen()
            if Whether_save_recording is True:
                recording_data = base64.b64decode(data)
                with open(recording_path, 'wb') as f:
                    f.write(recording_data)
            else:
                pass
        except Exception as e:
            logger.error(f'{[case_name]}停止屏幕录制失败，原因是{e}')
            raise e
        else:
            allure.attach(name=case_name+' 的测试录屏', body=base64.b64decode(data), attachment_type=allure.attachment_type.MP4)
            logger.info(f'{[case_name]}停止屏幕录制！！！')



if __name__=='__main__':
    driver=start_app()
    time.sleep(5)
    #element_operate(driver).swipe_element(info='test_bluetooth',start_location=[250,10],end_location=[250,400])
    #element_operate(driver).tap_element(info='test_bluetooth',location=[(122,178),(130,180)])
    #element_operate(driver).screen_shot('MAIN')
    #element_operate(driver).start_recording_screen('test')
    #time.sleep(10)
    #element_operate(driver).stop_recording_screen('test')
    element_operate(driver).click_element(loc=(By.XPATH,'//*[@text=\'{}\']'.format('① 注册')),info='主界面')
    element_operate(driver).menu_button(info='方案列表界面')





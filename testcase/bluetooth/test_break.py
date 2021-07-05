from element.bluetooth_page import Bluetooth_Page as Bluetooth
from operate.bluetooth_section import operate_packaging
from common.element_operate import element_operate
from element.main_page import Main_Page as Main
from common.public import threading_function
from selenium.webdriver.common.by import By
from common.start_app import start_app
from common.logger import logger
from common.public import level_
from common.app_operate import *
from threading import Thread
from time import sleep
import allure
import pytest

sign=False

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("异常测试")
@allure.feature("页面来回切换测试")
class Test_break():

    def break_(self):
        operate_packaging(self.driver).bluetooth_connect()
        for i in range(0,100):
            element_operate(self.driver).click_element(loc=Main.bluetooth_sign, info='Main')
            element_operate(self.driver).return_button(current_info='Main', return_info='Bluetooth')
        global sign
        sign=True

    def main(self):
        while True:
            if sign == True:
                break

    def app_process_(self):
        app_process()
        global sign
        sign=True

    def app_bluetooth_(self):
        app_bluetooth()
        global sign
        sign=True

    def setup(self):
        self.driver=start_app()
        operate_packaging(self.driver).open_bluetooth_message()
        logger.info('----------------测试开始-------------------')

    def teardown(self):
        self.driver.close_app()

        logger.info('-----------------测试结束-------------------')
    """
    @allure.story("用例--蓝牙点击连接")
    @allure.description("该用例是蓝牙正常点击连接功能测试")
    @allure.title('蓝牙点击连接测试')
    @level_('HIGH')
    def test_connect_bluetooth(self):
        operate_packaging(self.driver).bluetooth_connect()
        is_success = element_operate.is_exist_element(driver=self.driver,loc=Main.bluetooth_sign,info='MAIN')
        assert is_success
        element_operate(self.driver).click_element(loc=Main.bluetooth_sign,info='MAIN')
        element_operate(self.driver).press_element(loc=Bluetooth.bluetooth_number,info='BLUETOOTH')
        sleep(3)
    """
    @allure.story("用例--[Main]-->[Bluetooth]")
    @allure.description("该用例[Main]-->[Bluetooth]页面来回切换测试")
    @allure.title('[Main]-->[Bluetooth]')
    @level_('HIGH')
    def test_main(self):
       threading_function([self.main,self.break_,self.app_process_])
       assert element_operate(self.driver).get_element(loc=Main.bluetooth_sign,info='Main')



if __name__=='__main__':
    pytest.main(['-s','-v','test_break.py'])


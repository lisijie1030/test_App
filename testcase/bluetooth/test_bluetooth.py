from element.bluetooth_page import Bluetooth_Page as Bluetooth
from common.element_operate import element_operate
from element.main_page import Main_Page as Main
from common.public import assert_testcase
from common.logger import logger
from common.public import level_
import pytest
import allure


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("蓝牙连接测试")
@allure.feature("蓝牙正常连接")
class Test_Bluetooth():


    @allure.story("用例--蓝牙点击连接")
    @allure.description("该用例是蓝牙点击连接测试")
    @allure.title('蓝牙点击连接测试')
    @level_('HIGH')
    @assert_testcase
    def test_click_connect(self,fixture_start_app):
        driver=fixture_start_app
        app=element_operate(driver)
        app.click_element(loc=Main.bluetooth_sign,info='主页面')
        app.click_element(loc=Bluetooth.bluetooth_number,info='蓝牙连接界面')
        app.get_element_toast(loc=Bluetooth.bluetooth_connect_success,info='蓝牙连接成功')
        app.wait_element(loc=Main.bluetooth_sign,info='主界面')
        logger.info('自动切换到主界面')


    @allure.story("用例--蓝牙长按连接")
    @allure.description("该用例是蓝牙长按连接测试")
    @allure.title('蓝牙长按连接测试')
    @level_('HIGH')
    @assert_testcase
    def test_long_press_connect(self,fixture_start_app):
        driver=fixture_start_app
        app=element_operate(driver)
        app.click_element(loc=Main.bluetooth_sign,info='主页面')
        app.press_element(loc=Bluetooth.bluetooth_number,info='蓝牙连接界面')
        app.click_element(loc=Bluetooth.long_press_connect,info='蓝牙连接界面')
        app.get_element_toast(loc=Bluetooth.bluetooth_connect_success, info='蓝牙连接成功')
        app.wait_element(loc=Main.bluetooth_sign, info='主界面')
        logger.info('自动切换到主界面')



if __name__=='__main__':
    pytest.main(['-s','-v','test_bluetooth.py'])


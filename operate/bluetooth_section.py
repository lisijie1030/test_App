from common.logger import logger
from common.element_operate import element_operate
from element.main_page import Main_Page as MAIN
from element.bluetooth_page import Bluetooth_Page as BLUETOOTH
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import pytest



class bluetooth_section(element_operate):


    #判断APP程序是否崩溃
    def app_break(self):
        try:
            WebDriverWait(self.driver,500,5).until(lambda x:x.find_element(*MAIN.app_break))
        except Exception:
            pass
        else:
            logger.error('APP程序崩溃')

    #判断蓝牙是否异常断开
    def bluetooth_abnormal(self):
        try:
            WebDriverWait(self.driver,500,5).until(lambda x:x.find_element(*MAIN.bluetooth_abnormal))
        except Exception:
            pass
        else:
            logger.error('APP蓝牙异常断开')

    #蓝牙打开提示框
    def open_bluetooth_message(self):
        try:
            WebDriverWait(self.driver,3,0.5).until(lambda x:x.find_element(*MAIN.request_open_bluetooth))
        except Exception:
            pass
        else:
            self.click_element(loc=MAIN.allow_button, info='MAIN')
            self.is_exist_element(loc=MAIN.success_open_bluetooth_message,info='MAIN')

    #蓝牙连接
    def bluetooth_connect(self):
        self.click_element(loc=MAIN.bluetooth_sign, info='MAIN')
        self.click_element(loc=BLUETOOTH.bluetooth_number, info='BLUETOOTH')
        self.get_element_toast(loc=BLUETOOTH.bluetooth_connect_success, info='BLUETOOTH')

    #断开手机蓝牙再连接
    def break_bluetooth(self):
        self.swipe_element(info='MAIN',start_location=[250,10],end_location=[250,400])
        self.tap_element(info='MAIN',location=[(122,178),(130,180)])
        self.return_button(current_info='下拉通知框',return_info='MAIN')







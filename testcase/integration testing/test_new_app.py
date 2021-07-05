from common.element_operate import element_operate
from common.start_app import start_app
from element.bluetooth_page import Bluetooth_Page as Bluetooth
from element.main_page import Main_Page as Main
from element.itemdowload_page import Itemdownload_Page as Item
from element.register_page import Register_Page as Register
from element.networking_page import Networking_page as Networking
from element.detonated_page import Detonated_page as Detonated
from element.historyrecord_page import Historyrecord_page as History
from common.logger import logger
from common.read_file import read_excel
from config.file_path import data_path
import pytest
import time


class Test_new_app():

    """
    def setup(self):
        self.driver=start_app()
        logger.info('=================================测试开始==================================')

    def teardown(self):
        self.driver.close_app()
        logger.info('=================================测试结束==================================')
    """

    def test_new_app(self,fixture_start_app):

        #蓝牙连接
        app=element_operate(fixture_start_app)
        app.click_element(loc=Main.bluetooth_page,info='主界面')
        app.click_element(loc=Bluetooth.bluetooth_connect,info='蓝牙连接界面')
        assert app.is_exist_element(loc=Bluetooth.bluetooth_connect_status,info='蓝牙连接界面',timeout=10)
        device_num=app.get_element_text(loc=Bluetooth.bluetooth_device,info='蓝牙连接界面')
        logger.info(f'当前连接的起爆器编号为：{device_num}')
        app.return_button(current_info='蓝牙连接界面',return_info='主界面')

        #注册
        app.click_element(loc=Main.register_page,info='主界面')
        app.menu_button(info='方案列表界面')
        app.click_element(loc=Register.import_from_file,info='方案列表界面')
        app.click_element(loc=Register.data_file,info='方案列表界面')
        #assert app.is_exist_element(loc=Register.success_import_file,info='方案列表界面',timeout=5)
        app.click_element(loc=Register.project,info='方案列表加载界面')
        app.return_button(current_info='注册方案界面',return_info='主界面')

        """
        app.input_element(loc=Register.hole_num,info='初始化方案界面',msg=10)
        app.click_element(loc=Register.add_Btn,info='初始化方案界面')
        app.return_button(current_info='初始化方案界面',return_info='注册方案界面')
        app.click_element(loc=Register.start_register_Btn,info='注册方案界面')
        app.click_element(loc=Register.input_bind,info='注册界面')
        UID=read_excel(path=f'{data_path}/LG.xlsx',line_num=1)
        code=read_excel(path=f'{data_path}/LG.xlsx',line_num=0)
        for i in range(0,9):
            app.input_element(loc=Register.input_uid,info='注册界面',msg=UID[i])
            app.input_element(loc=Register.input_code,info='注册界面',msg=code[i])
            app.click_element(loc=Register.input_bind_comfirm,info='注册界面')
        app.return_button(current_info='注册页面',return_info='注册方案页面')
        app.return_button(current_info='注册方案界面',return_info='主界面')
        """

        #项目下载
        app.click_element(loc=Main.itemdownload_page,info='主界面')
        app.click_element(loc=Item.download_Btn_before,info='项目信息')
        app.click_element(loc=Item.download_Btn_after,info='项目下载')
        time.sleep(2)
        app.return_button(current_info='项目下载',return_info='项目信息')
        app.return_button(current_info='项目信息',return_info='主界面')

        #组网
        app.click_element(loc=Main.networking_page,info='主界面')
        #app.click_element(loc=Networking.comfirm_Btn,info='组网界面')
        time.sleep(1)
        app.swipe_element(start_location=[400,500],end_location=[100,500],info='组网界面')
        app.click_element(loc=Networking.networking_Btn,info='组网界面')
        time.sleep(2)
        assert app.is_exist_element(loc=Networking.networking_Btn,info='组网界面',timeout=100)
        app.return_button(current_info='组网界面',return_info='组网界面')

        #起爆
        app.click_element(loc=Main.detonated_page,info='主界面')
        app.click_element(loc=Detonated.charge_Btn,info='充电起爆界面')
        assert app.is_exist_element(loc=Detonated.detonated_Btn,info='充电起爆界面',timeout=100)
        app.click_element(loc=Detonated.detonated_Btn,info='充电起爆界面')
        first=app.get_element_text(loc=Detonated.fist_code,info='输入验证码界面')
        second=app.get_element_text(loc=Detonated.second_code,info='输入验证码界面')
        third=app.get_element_text(loc=Detonated.third_code,info='输入验证码界面')
        fourth=app.get_element_text(loc=Detonated.fourth_code,info='输入验证码界面')
        app.input_element(loc=Detonated.input_code,info='输入验证码界面',msg=first+second+third+fourth)
        app.click_element(loc=Detonated.comfirm_Btn,info='输入验证码界面')
        app.return_button(current_info='输入验证码界面',return_info='充电起爆界面')
        app.click_element(loc=Detonated.discharge_Btn,info='充电起爆界面')
        assert app.is_exist_element(loc=Detonated.charge_Btn,info='充电起爆界面',timeout=5)
        app.return_button(current_info='充电起爆界面',return_info='主界面')


        app.click_element(loc=Main.register_page,info='主界面')
        app.menu_button(info='注册方案界面')
        app.click_element(loc=Register.load_project,info='注册方案界面')
        app.press_element(loc=Register.project,info='方案列表界面',duration=1000)
        app.click_element(loc=Register.delete_project,info='方案列表界面')
        app.return_button(current_info='方案列表界面',return_info='主界面')

        """
        app.click_element(loc=Detonated.boom_Btn,info='起爆界面')
        assert app.is_exist_element(loc=History.upload_Btn,info='爆破历史界面',timeout=10)
        app.return_button(current_info='爆破历史界面',return_info='主界面')
        """


if __name__=='__main__':
    pytest.main(['-s','-v','test_new_app.py'])











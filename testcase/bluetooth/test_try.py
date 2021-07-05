from element.register_page import Register_Page as Register
from operate.bluetooth_section import bluetooth_section
from common.element_operate import element_operate
from element.main_page import Main_Page as Main
from common.start_app import start_app
from common.logger import logger
from time import sleep
import pytest
from common.public import data_report
from common.public import assert_testcase




class Test_try():

    """
    def setup(self):
        self.driver=start_app()

    def teardown(self):
        self.driver.close_app()




    @pytest.fixture(scope='function',autouse=True)
    def fixture_ready(self):
        logger.info('======================测试开始=====================')
        self.driver = start_app()
        yield
        logger.info('======================测试结束=====================')
        self.driver.close_app()

    """
    @assert_testcase
    def test_try(self,fixture_start_app):
        self.driver=fixture_start_app
        #data_report(path='C:/Users/lisijie/PycharmProjects/起爆器APP测试/data/test_data.xlsx')
        #element_operate(self.driver).start_recording_screen('test')
        bluetooth_section(self.driver).bluetooth_connect()
        #assert element_operate.is_exist_element(self.driver, loc=Main.bluetooth_sign, info='Main')
        for i in range(0, 10):
            element_operate(self.driver).click_element(loc=Main.register, info='Main')
            element_operate(self.driver).click_element(loc=Register.return_btn, info='Register')
            # assert element_operate.is_exist_element(self.driver, loc=Main.bluetooth_sign, info='注册')
        # element_operate(self.driver).stop_recording_screen('test')



    @pytest.mark.skip("aa")
    def test_01(self):
        print('开始等待...')
        sleep(20)
        print('等待结束...')

if __name__=='__main__':
    pytest.main(['-s','-v','test_try.py'])
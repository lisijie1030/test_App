from common.read_file import read_yaml
from common.logger import logger
from config.file_path import *
from appium import webdriver

app_data=read_yaml(app_config_data_path)['新版APP']


def start_app():
    desired_caps = {}
    desired_caps['platformName'] = app_data['platformName']
    desired_caps['deviceName'] = app_data['deviceName']
    desired_caps['appPackage'] = app_data['appPackage']
    desired_caps['appActivity'] = app_data['appActivity']
    desired_caps['noReset'] = app_data['noReset']
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        driver.implicitly_wait(2)
        logger.info('-------------APP连接成功-------------')
    except Exception as e:
        logger.error(f'APP连接失败,原因是{e}')
    else:
        return driver

if __name__=='__main__':
    start_app()



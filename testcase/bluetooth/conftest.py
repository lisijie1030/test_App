from common.app_operate import single_bluetooth_whether_connect,single_app_whether_process
from common.element_operate import element_operate
from common.start_app import start_app,logger
import pytest
import os
"""
driver=None

@pytest.fixture(scope='function', autouse=True)
def fixture_start_app():
    logger.info('======================测试开始=====================')
    global driver
    if driver is None:
        driver = start_app()
    yield driver
    logger.info('======================测试结束=====================')
    driver.close_app()
    driver = None



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
   
    hook pytest失败
    :param item:
    :param call:
    :return:
    
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
        
        #失败用例自动截图
        element_operate(driver=driver).screen_shot(info='bluetooth')
        #判断蓝牙是否断开
        single_bluetooth_whether_connect()
        #判断APP进程是否被杀掉
        single_app_whether_process(apk='factory.dev')

"""

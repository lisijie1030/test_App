from common.app_operate import allure_report,allure_html
from user import Whether_report
import pytest
import time

test_section='bluetooth'
test_case='test_bluetooth.py'

report_name=str(test_case).split('.')[0]+'-'+time.strftime('%Y-%m-%d')
report_path='./report/'+report_name

class MyPlugin(object):
    def pytest_sessionfinish(self):
        print( f'#################################################### --- {test_case} finishing --- ####################################################')


if __name__=='__main__':
    if Whether_report == False:
        pytest.main(['-s', '-v', f'./testcase/{test_section}/{test_case}'])
        MyPlugin().pytest_sessionfinish()
    if Whether_report == True:
        pytest.main(['-s', '-v', f'./testcase/{test_section}/{test_case}', f'--alluredir={report_path}'])
        MyPlugin().pytest_sessionfinish()
        allure_report(path=report_path)
        #allure_html(report_name=report_name)

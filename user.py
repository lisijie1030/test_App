from common.send_emai import email

Whether_screenshot=True

Whether_report=True

Whether_email=False

Whether_save_recording=False

#生成测试报告
"allure serve report/'报告包名'"
#生成测试报告.html文件
"allure generate report/'报告包名' -o report/allure_report --clean"


if Whether_email==True:
    email(report_file='./report/allure_report/index.html')
else:
    pass


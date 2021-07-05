from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.logger import logger
from email.header import Header
import smtplib


def email(report_file):
    msg=MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'allure_report','utf-8'))
    msg['From']='1390090207@qq.com'
    msg['To']='3285590346@qq.com'
    msg['Subject']=Header('测试报告','utf-8')
    att=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']="attachment;filename='report.allure_report'"
    msg.attach(att)
    try:
        smtp=smtplib.SMTP_SSL('smtp.qq.com')
        smtp.login('1390090207@qq.com','filpvtgnkjgegjji')
        smtp.sendmail('1390090207@qq.com','3285590346@qq.com',msg.as_string())
        logger.info('邮件发送成功!!!')
        smtp.quit()
    except Exception as e:
        logger.error(f'邮件发送失败，原因是{e}')



if __name__=='__main__':
    email(report_file='../report/allure_report/index.html')

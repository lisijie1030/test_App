
import logging
import time
import os


base_path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(base_path, 'log')
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Logger():

    def __init__(self):
        # 日志初始化
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 设置日志名
        self.log_name = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
        # 日志格式设置（定义）
        self.formater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        # 日志输出到文件（定义）
        self.filelogger = logging.FileHandler(self.log_name, mode='a', encoding="UTF-8")
        # 日志输出到控制台（定义）
        self.console = logging.StreamHandler()
        # 设置日志LEVEL
        self.filelogger.setLevel(logging.INFO)
        self.console.setLevel(logging.INFO)
        # 设置日志输出格式（实施）
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        # 日志文件形式加载（实施）
        self.logger.addHandler(self.filelogger)
        # 日志控制台形式加载（实施）
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info('----测试开始----')
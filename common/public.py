from common.logger import logger
from threading import Thread
from functools import wraps
import inspect
import time
from openpyxl import load_workbook
import allure

#获取当前运行的方法名
def get_func_name():
    return inspect.stack()[1][3]


#判断数据类型
def typeof(variate):
    type=None
    if isinstance(variate,int):
        type = "int"
    elif isinstance(variate,str):
        type = "str"
    elif isinstance(variate,float):
        type = "float"
    elif isinstance(variate,list):
        type = "list"
    elif isinstance(variate,tuple):
        type = "tuple"
    elif isinstance(variate,dict):
        type = "dict"
    elif isinstance(variate,set):
        type = "set"
    return type


#返回数据类型
def getType(variate):
    arr = {"int":"整数","float":"浮点","str":"字符串","list":"列表","tuple":"元组","dict":"字典","set":"集合"}
    vartype = typeof(variate)
    if not (vartype in arr):
        return "未知类型"
    return arr[vartype]


#多线程函数封装
def threading_function(loc):
    """
    :param loc: 函数名称，列表形式 如[x_1,x_2]第一个函数为主线程，其余为守护线程
    :return:
    """
    if getType(loc)=='列表':
        try:
            function_number = len(loc)
            for i in range(0, function_number):
                func = Thread(target=loc[i])
                if i != 0:
                    func.setDaemon(True)
                func.start()
                logger.info(f'线程{loc[i]}正在进行中......')
            loc[0]()
        except Exception as e:
            logger.error(f'线程{loc}进行失败，原因是{e}')
    else:
        logger.error(f'{loc}输入格式有误！！！')


#持续时间（装饰器）
def time_(func):
    @wraps(func)
    def duration_(*args,**kwargs):
        start_time=time.time()
        func(*args,*kwargs)
        end_time=time.time()
        logger.info(f'{[func.__name__]}--所用时间-->{round((end_time-start_time),2)}秒')
    return duration_


#测试用例级别（装饰器）
def level_(level):
   def wrapper(func):
       @wraps(func)
       def inner_wrapper(*args, **kwargs):
           logger.info(f"{[func.__name__]}--level-->{[level]}")
           return func(*args, **kwargs)
       return inner_wrapper
   return wrapper



#页面切换（装饰器）
def app_activity_(start_activity,end_activity):
    def wrapper(func):
        def get_activity(*args,**kwargs):
            print(f'当前页面是{start_activity}，切换到的页面是{end_activity}')
            return func(*args,**kwargs)
        return get_activity
    return wrapper



#测试用例名字（装饰器）
def test_case_(name):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args,**kwargs):
            logger.info(f'{[func.__name__]}当前的测试用例为------->{name}')
            return func(*args,**kwargs)
        return inner_wrapper
    return wrapper



#测试环境（装饰器）
def test_environment_(envirnment):
    def wrapper(func):
        @wrapps(func)
        def inner_wrapper(*args,**kwargs):
            logger.info(f'{[func.__name__]}当前的测试环境为--------->{envirnment}')
            return func(*args,**kwargs)
        return inner_wrapper
    return wrapper



#异常判断（装饰器）
def assert_testcase(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as e:
            logger.error(f'{[func.__name__]}测试用例运行失败，原因是{e}')
            assert(False)
    return wrapper



#测试数据导入报告中
def data_report(path):
    wb=load_workbook(path)
    sheet=wb['Sheet1']
    data=''
    for line in sheet.rows:
        for value in line:
            data=data+str(value.value)+','
        data=data+'\n'
    allure.attach(data,'测试数据',attachment_type=allure.attachment_type.CSV)



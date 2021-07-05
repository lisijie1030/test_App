from common.public import threading_function
from common.public import get_func_name
from config.file_path import app_path
from common.logger import logger
from functools import wraps
import time
import os


#判断设备是否连接（装饰器）
def whether_connect(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            if device_connect():
                return func(*args,**kwargs)
            else:
                logger.info('设备未连接，请重新连接')
        except Exception as e:
            logger.error(f'{[get_func_name()]}:发生异常错误，原因是{e}')
            raise e
    return wrapper



def device_connect():
    """
    判断手机是否连接
    ADB命令：adb devices
    :return: Bool
    """
    try:
        with os.popen('adb devices') as device_info:
            device=device_info.readlines()
            if device[1]=='\n':
                return False
            else:
                return True
    except Exception as e:
        logger.error(f'{[get_func_name()]}:发生异常错误，原因是{e}')



@whether_connect
def get_device_name():
    """
    获取设备名
    ADB命令：adb devices
    :return: name-->设备名称
    """
    with os.popen('adb devices') as devices_name:
        name = devices_name.readlines()[1].split('\t')[0]
        logger.info(f'当前连接的设备名为：{name}')
        return name



@whether_connect
def get_device_version():
    """
    获取设备版本
    ADB命令：adb shell getprop ro.build.version.release
    :return: version-->设备版本号
    """
    with os.popen('adb shell getprop ro.build.version.release') as device_version:
        version = device_version.read()
        logger.info(f'当前连接设备的版本号为: Android {version}')
        return version



@whether_connect
def bluetooth_whether_connect():
    """
    循环判断APP的蓝牙是否断开
    ADB命令：adb shell dumpsys bluetooth_manager | findstr Connections
    :return:
    """
    logger.info('开始判断APP的蓝牙是否断开')
    while True:
        with os.popen('adb shell dumpsys bluetooth_manager | findstr Connections') as bluetooth_connect:
            bluetooth = bluetooth_connect.readlines()
            result=len(bluetooth)
            if result == 2:
                logger.error('APP蓝牙已断开')
                break


@whether_connect
def single_bluetooth_whether_connect():
    with os.popen('adb shell dumpsys bluetooth_manager | findstr Connections') as bluetooth_connect:
        bluetooth = bluetooth_connect.readlines()
        result = len(bluetooth)
        if result == 3:
            logger.info('APP蓝牙未断开')
        else:
            logger.error('APP蓝牙已断开')



@whether_connect
def get_bluetooth_address():
    """
    获取手机连接的蓝牙地址
    ADB命令：adb shell dumpsys bluetooth_manager
    :return: address-->蓝牙地址
    """
    with os.popen('adb shell dumpsys bluetooth_manager') as bluetooth_address:
        bluetooth = bluetooth_address.readlines()
        lines = []
        for line in bluetooth:
            if 'Connections' in line:
                lines.append(line)
        num = bluetooth.index(lines[0])
        address = bluetooth[num + 1].split()[5]
        logger.info(f'APP连接的蓝牙设备的地址为:{address}')
        return address


@whether_connect
def app_whether_process(apk):
    """
    循环判断APP的进程是否还在运行中
    ADB命令：adb shell dumpsys activity activities
    ADB命令：adb shell ps
    :param apk: APP包名
    :return:
    """
    logger.info(f'开始判断APP的进程是否还在运行中')
    while True:
        with os.popen('adb shell dumpsys activity activities') as activity_app:
            activity = activity_app.read()
            result1 = f'{apk}' in activity
            if result1 == True:
                pass
            else:
                with os.popen('adb shell ps') as process_app:
                    process_information = process_app.read()
                    result2 = f'{apk}' in process_information
                    if result2 == True:
                        logger.error('APP的activity已被杀死,但是进程还在')  # APP程序崩溃
                        break
                    else:
                        logger.error('APP的进程已被杀死')
                        break


@whether_connect
def single_app_whether_process(apk):
    with os.popen('adb shell dumpsys activity activities') as activity_app:
        activity = activity_app.read()
        result1 = f'{apk}' in activity
        if result1 == True:
            logger.info('APP的进程未被杀死！')
        else:
            with os.popen('adb shell ps') as process_app:
                process_information = process_app.read()
                result2 = f'{apk}' in process_information
                if result2 == True:
                    logger.error('APP的activity已被杀死,但是进程还在！')  # APP程序崩溃
                else:
                    logger.error('APP的进程已被杀死!')



@whether_connect
def app_whether_background(apk):
    """
    循环判断APP是否在后台运行
    ADB命令：adb shell dumpsys activity factory.dev
    :return:
    """
    logger.info(f'开始判断APP是否已切到后台运行')
    while True:
        with os.popen(f'adb shell dumpsys activity {apk}') as devices_status:
            devices_information = devices_status.read()
            result = 'mStateSaved=false mStopped=false' in devices_information
            if result == True:
                pass
            else:
                logger.info('APP已切换到后台运行')
                break



@whether_connect
def single_app_whether_background(apk):
    """
    判断APP是否在后台运行
    ADB命令：adb shell dumpsys activity factory.dev
    :return:
    """
    logger.info(f'开始判断APP是否已切到后台运行')
    with os.popen(f'adb shell dumpsys activity {apk}') as devices_status:
        devices_information = devices_status.read()
        result = 'mStateSaved=false mStopped=false' in devices_information
        if result == True:
            pass
        else:
            logger.info('APP已切换到后台运行')



@whether_connect
def app_whether_foreground(apk):
    """
    循环判断APP是否在前台运行
    ADB命令：adb shell dumpsys activity factory.dev
    :param apk: APP包名
    :return:
    """
    logger.info(f'开始判断APP是否已切到前台运行')
    while True:
        with  os.popen(f'adb shell dumpsys activity {apk}') as devices_status:
            devices_information = devices_status.read()
            result = 'mStateSaved=true mStopped=true' in devices_information
            if result == True:
                pass
            else:
                logger.info('APP已切换到前台运行')
                break




@whether_connect
def single_app_whether_foreground(apk):
    """
    判断APP是否在前台运行
    ADB命令：adb shell dumpsys activity factory.dev
    :param apk: APP包名
    :return:
    """
    logger.info(f'开始判断APP是否已切到前台运行')
    with  os.popen(f'adb shell dumpsys activity {apk}') as devices_status:
        devices_information = devices_status.read()
        result = 'mStateSaved=true mStopped=true' in devices_information
        if result == True:
            pass
        else:
            logger.info('APP已切换到前台运行')




@whether_connect
def get_cpu_data(apk):
    """
    获取手机CPU数据
    ADB命令：adb shell top -m 100 -n 1 -d 1 -s 9 | findstr apk
    :param apk: APP包名
    :return: data-->cpu数据
    """
    logger.info('开始获取CPU数据')
    with os.popen(f' adb shell top -m 100 -n 1 -d 1 -s 9 | findstr {apk}') as get_cpu:
        cpu_data = get_cpu.readline().split(' ')
        if cpu_data == ['']:
            data = '0.0'
        else:
            data = list(filter(None, cpu_data))[8]
        return data





@whether_connect
def get_memory_data(apk):
    """
    获取手机内存数据
    ADB命令：adb shell dumpsys meminfo apk | findstr PSS
    :param apk: APP包名
    :return: data-->内存数据
    """
    logger.info('开始获取内存数据')
    with os.popen(f'adb shell dumpsys meminfo {apk} | findstr PSS') as get_memory:
        memory_data = get_memory.readline().split(' ')
        if memory_data == ['']:
            data = '0.0'
        else:
            data = round((float(list(filter(None, memory_data))[1]) / 1024), 2)
        return data




@whether_connect
def install_app(app_path):
    """
    安装APP
    ADB命令：adb install app_path
    :param app_path: APP存放地址
    :return:
    """
    logger.info('开始安装APP')
    with os.popen(f'adb install {app_path}') as result_file:
        result = result_file.read()
        if 'Success' in result:
            logger.info('APP安装成功')
        else:
            logger.error('APP安装异常')




@whether_connect
def uninstall_app(apk):
    """
    卸载APP
    ADB命令：adb uninstall apk
    :param apk: APP包名
    :return:
    """
    logger.info('开始卸载APP')
    with os.popen(f'adb uninstall {apk}') as result_file:
        result = result_file.read()
        if 'Success' in result:
            logger.info('APP卸载成功')
        else:
            logger.error('APP卸载异常')




@whether_connect
def start_appium():
    """
    启动APPIUM
    有问题，待改进
    :return:
    """
    path = 'C:\\Users\\lisijie\\Desktop\\start_appium.bat'
    os.system(path)


@whether_connect
def stop_appium():
    """
    关闭APPIUM，需要按键
    ADB命令：netstat -aon|findstr 4723
    ADB命令：taskkill -f -pid '进程数'
    :return:
    """
    with os.popen('netstat -aon|findstr 4723') as result1:
        process = result1.read().split()
        if len(process) == 0:
            logger.info('4723端口未被占用')
        else:
            process_number = process[4]
            with os.popen(f'taskkill -f -pid {process_number}') as result2:
                sucess = result2.read()
                if '成功' in sucess:
                    logger.info('appium进程结束')
                else:
                    logger.error('appium进程未正常结束')



def close_cmd():
    """
    关闭cmd进程(关闭appium,无需按键）
    :return:
    """
    os.popen('taskkill -f -t -im cmd.exe')



def allure_report(path):
    """
    生成Allure报告
    allure命令：allure serve '测试报告绝对路径'
    :param report_name: 报告名
    :return:
    """
    try:
        os.popen(f'allure serve {path}')
    except Exception as e:
        logger.error(f'{[get_func_name()]}:发生异常错误，原因是{e}')
    else:
        report_name=path.split('/')[-1:]
        logger.info(f'测试报告: {report_name} 已成功打开')



def allure_html(path):
    """
    生成html文件
    新生成的HTML文件将会替换到原来的文件
    allure命令:allure generate '测试报告绝对路径' -o report/allure_report --clean
    :param report_name:
    :return:
    """
    try:
        os.popen(f'allure generate {path} -o report/allure_report --clean')
    except Exception as e:
        logger.error(f'{[get_func_name()]}:发生异常错误，原因是{e}')
    else:
        report_name=path.split('/')[-1:]
        logger.info(f'测试报告: {report_name} 已成功生成html文件')



#app_process()
#app_foreground()
#app_background()
#app_bluetooth()
#start_appium()
#app_process(apk='factory.dev')
#stop_appium()
#start_appium()
#get_cpu_data(apk='prod.prod')
#get_memory_data(apk='factory.dev')
#allure_report('test_tr-2021-05-25')
#bluetooth_whether_connect()
#get_bluetooth_address()
#bluetooth_whether_connect()
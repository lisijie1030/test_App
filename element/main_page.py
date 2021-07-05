from selenium.webdriver.common.by import By

class Main_Page():


    """
    #程序异常崩溃提示框
    app_break=(By.ID,'android:id/alertTitle')
    #app_break=(By.XPATH,'//*[@text=\'{}\']'.format('FHL试爆器已停止运行'))

    #蓝牙连接异常]
    #bluetooth_abnormal=(By.ID,'factory.dev:id/alertTitle')
    bluetooth_abnormal=(By.XPATH,'//*[@text=\'{}\']'.format('蓝牙连接断开，是否重新连接'))

    #手机蓝牙关闭时弹出的提示框
    request_open_bluetooth=(By.XPATH,'//*[@text=\'{}\']'.format('FHL试爆器请求开启蓝牙'))

    #提示框中的允许按钮
    allow_button=(By.ID,'android:id/button1')

    #成功打开蓝牙提示语
    success_open_bluetooth_message=(By.XPATH,'//*[@text=\'{}\']'.format('打开蓝牙-1 成功'))

    #蓝牙连接的标志
    bluetooth_sign=(By.ID,'factory.dev:id/ac_lgmain_img_but_bluetooth')

    #注册
    register=(By.XPATH,'//*[@text=\'{}\']'.format('① 注册'))


    """
    #程序崩溃
    process_mistake=(By.ID,'com.fhl.ed.initiator3:id/md_text_title')

    #蓝牙连接界面
    bluetooth_page=(By.ID,'com.fhl.ed.initiator3:id/device_name')

    #注册界面
    register_page=(By.XPATH,'//*[@text=\'{}\']'.format('① 注册'))

    #项目下载界面
    itemdownload_page=(By.XPATH,'//*[@text=\'{}\']'.format('② 项目下载'))

    #组网界面
    networking_page=(By.XPATH,'//*[@text=\'{}\']'.format('③ 组网'))

    #起爆界面
    detonated_page=(By.XPATH,'//*[@text=\'{}\']'.format('④ 起爆'))


















from selenium.webdriver.common.by import By

class Bluetooth_Page():

    """
    #起爆器标编号
    bluetooth_number = (By.XPATH, '//*[@text=\'{}\']'.format('1770000025'))

    #蓝牙连接成功标志
    bluetooth_connect_success = (By.XPATH, '//*[@text=\'{}\']'.format('连接成功'))

    #长按起爆器显示连接
    long_press_connect=(By.XPATH, '//*[@text=\'{}\']'.format('连接'))

    #长按起爆器显示删除
    long_press_delete=(By.XPATH, '//*[@text=\'{}\']'.format('删除'))

    #长按起爆器显示删除
    long_press_cancel=(By.XPATH, '//*[@text=\'{}\']'.format('取消'))

    """

    bluetooth_connect = (By.ID, 'com.fhl.ed.initiator3:id/device_connection_state')

    bluetooth_connect_status=(By.XPATH,'//*[@text=\'{}\']'.format('已连接，点击取消连接'))

    bluetooth_device =(By.ID,'com.fhl.ed.initiator3:id/device_sn')
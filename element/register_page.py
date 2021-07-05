from selenium.webdriver.common.by import By

class Register_Page():

    """
    start_register_btn=(By.XPATH,'//*[@text=\'{}\']'.format('开始注册'))

    return_btn=(By.CLASS_NAME,'android.widget.ImageButton')

    """
    initialization_scheme_Btn=(By.ID,'com.fhl.ed.initiator3:id/init_project')

    import_from_file=(By.ID,'com.fhl.ed.initiator3:id/title')

    data_file=(By.XPATH,'//*[@text=\'{}\']'.format('data.csv'))

    success_import_file=(By.XPATH,'//*[@text=\'{}\']'.format('✔ 导入方案成功!'))

    project=(By.ID,'com.fhl.ed.initiator3:id/view')

    hole_num=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                       'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                       'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                       'android.view.ViewGroup/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/'
                       'androidx.appcompat.widget.LinearLayoutCompat[3]/android.widget.LinearLayout[1]/'
                       'android.widget.FrameLayout/android.widget.EditText')

    add_Btn=(By.ID,'com.fhl.ed.initiator3:id/confirm_add')

    start_register_Btn=(By.ID,'com.fhl.ed.initiator3:id/register')

    input_bind=(By.ID,'com.fhl.ed.initiator3:id/input_bind')

    input_uid=(By.ID,'com.fhl.ed.initiator3:id/uid')

    input_code=(By.ID,'com.fhl.ed.initiator3:id/sid')

    input_bind_comfirm=(By.ID,'com.fhl.ed.initiator3:id/input_bind_confirm')

    #bind_success=(By.XPATH,'//*[@text=\'{}\']'.format(''))

    #加载方案
    load_project=(By.XPATH,'//*[@text=\'{}\']'.format('加载方案'))

    #删除方案
    delete_project=(By.XPATH,'//*[@text=\'{}\']'.format('删除'))









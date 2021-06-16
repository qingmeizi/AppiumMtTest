from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction

class OrderSecondPage(BaseAction):
    #提交订单按钮
    orderSecond_confirm = By.XPATH,"text,提交订单"
    #第一支付密码框
    one_password_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText\n"
    #第二支付密码框
    two_password_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]\n"
    #第三支付密码框
    three_password_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[2]\n"
    #第四支付密码框
    four_password_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[3]\n"
    #第五支付密码框
    five_password_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[4]\n"
    #第六支付密码框
    six_password_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[5]\n"


    def __init__(self, driver):
        self.driver = driver

    #点击提交订单
    def click_ordersecond_confirm(self):
        self.click(self.orderSecond_confirm)
    #输入第一个支付密码
    def one_password_box_input(self,text):
        self.input(self.one_password_box,text)
    #输入第二个支付密码
    def two_password_box_input(self,text):
        self.input(self.two_password_box,text)
    #输入第三个支付密码
    def three_password_box_input(self,text):
        self.input(self.three_password_box,text)
    #输入第四个支付密码
    def foure_password_box_input(self,text):
        self.input(self.four_password_box,text)
    #输入第五个支付密码
    def five_password_box_input(self,text):
        self.input(self.five_password_box,text)
    #输入第六个支付密码
    def six_password_box_input(self,text):
        self.input(self.six_password_box,text)




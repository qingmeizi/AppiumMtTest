from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction

class UserLoginPage(BaseAction):
    #手机登录
    mobile_login =By.XPATH,"//*[@text='手机登录']"
    #手机号
    mobie_box = By.ID,"com.maitao.mtqzy:id/mobileEdt"
    #密码
    password_box = By.ID,"com.maitao.mtqzy:id/codeEdt"
    # 勾选框
    check_box = By.ID, "com.maitao.mtqzy:id/privacyStateImg"
    #提交
    submit_button = By.ID,"com.maitao.mtqzy:id/submitTxt"

    #下次再说
    TheNext_button = By.ID,"com.maitao.mtqzy:id/nextTxt"



    def __init__(self,driver):
        self.driver = driver
    #点击手机登录
    def click_mobile_login(self):
        self.click(self.mobile_login)
    #输入手机号
    def mobile_input(self,mobile):

        self.input(self.mobie_box,mobile)
    #输入密码
    def password_input(self,password):
        self.input(self.password_box,password)
    #点击勾选
    def click_check_box(self):
        self.click(self.check_box)
    #点击提交
    def click_submit(self):
        self.click(self.submit_button)
    #下次再说
    def click_Next(self):
        self.click(self.TheNext_button)
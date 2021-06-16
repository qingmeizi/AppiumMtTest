from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction
class UserHmoePage(BaseAction):
    #登录/注册
    login_registered = By.ID,"com.maitao.mtqzy:id/nicknameTxt"
    #首页
    homepage_tab = By.XPATH,"//*[@text='首页']"

    def __init__(self, driver):
        self.driver = driver

    #点击登录/注册
    def click_login_registered(self):
        self.click(self.login_registered)
    #点击首页
    def click_homePage_tab(self):
        self.click(self.homepage_tab)
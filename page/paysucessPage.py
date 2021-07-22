from base.BaseAction import BaseAction
from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
class PaysucessPage(BaseAction):
    orderdetail_button = By.XPATH,"//*@text='订单详情']"
    def __init__(self,driver):
        self.driver = driver
    def click_orderdetail_button(self):
        self.click(self.orderdetail_button)


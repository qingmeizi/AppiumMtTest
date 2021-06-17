from base.BaseAction import BaseAction
from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
class PaysucessPage(BaseAction):
    orderdetail_button = By.XPATH,"//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[8]"
    def __init__(self,driver):
        self.driver = driver
    def click_orderdetail_button(self):
        self.click(self.orderdetail_button)


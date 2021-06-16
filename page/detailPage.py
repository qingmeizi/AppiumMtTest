from selenium.webdriver.common.by import By
from base.BaseAction import BaseAction

class DetailPage(BaseAction):

    #立即购买
    immediately_buy = By.XPATH,"//*[@text='立即购买']"

    def __init__(self, driver):
        self.driver = driver
    #点击立即购买
    def click_immediately_buy(self):
        self.click(self.immediately_buy)



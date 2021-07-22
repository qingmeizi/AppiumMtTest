from selenium.webdriver.common.by import By  # 导入By模块
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction
class BeforHomePage(BaseAction):
    #同意按钮
    agreen_button = By.XPATH,"//*[@text='同意']"
    #我知道了按钮
    Iknow_button = By.XPATH,"//*[@text='我知道了']"
    #首页第一个　下一步
    #first_Know = By.ID,"com.maitao.mtqzy:id/start_guide_banner_item_image"
    first_Know = By.XPATH,"//androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.ImageView"
    #首页第二个下一步
   # second_know = By.ID, "com.maitao.mtqzy:id/start_guide_banner_item_image"
    second_know = By.XPATH, "//androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.ImageView"
    # 首页第三个  我知道了
    #three_know = By.ID, "com.maitao.mtqzy:id/start_guide_banner_item_image"
    three_know = By.XPATH, "//androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.ImageView"
    #仅使用期间允许
    click_during = By.XPATH, "//*[@text = '仅使用期间允许']"




    #允许，选择城市
    allow_button = By.XPATH,"//*[@text='仅使用期间允许']"
    #取消定位
    cancel_button = By.XPATH,"//*[@text='取消']"
    #选中城市
    select_city = By.XPATH,"//*[@text='上海']"

    def __int__(self, driver):
        self.driver = driver

    #点击同意
    def click_agreen_button(self):
        self.click(self.agreen_button)
    #点击我知道了
    def click_Iknow(self):
        self.click(self.Iknow_button)
    #点击第一个我知道
    def click_first_know(self):
        self.click(self.first_Know)
    #点击第二个我知道
    def click_second_know(self):
        self.click(self.second_know)
    #点击第三个我知道
    def click_three_know(self):
        self.click(self.three_know)

    #仅使用期间允许
    def click_allow_during(self):
        self.click(self.click_during)

    #允许
    def click_allow_button(self):
        self.click(self.allow_button)

    #取消定位
    def click_cancel_button(self):
        self.click(self.cancel_button)
    #选中城市
    def click_select_city(self):
        self.click(self.select_city)






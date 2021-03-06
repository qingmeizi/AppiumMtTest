from selenium.webdriver.common.by import By  # 导入By模块
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction
class MainHmoePage(BaseAction):

    #我的
    my_tab = By.XPATH, "//*[@text='我的']"
   # my_tab = By.XPATH, "text，我的"

    #搜索框
    search_box = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]"
   #精选
    fine_select= By.XPATH,"//*[@text='精选']"

    #产品名称---预定的产品配置在首页的精选
    product_location = By.XPATH,"//*[@text='11月6日|《海贼王-ルフィ猛攻!》杭州剧院100元起超燃二次元交响电声音乐会！']"

    #测试产品83184

    #提示版本升级的弹窗，
    Afrer_say = By.XPATH, "//*[@text='以后再说']"

    def __int__(self, driver):
        self.driver = driver


    #点击我的
    def click_my_tab(self):
        self.click(self.my_tab)
    #点击搜索框
    def click_search_box(self):
        self.click(self.search_box)


    #点击精选
    def click_fine_select(self):
        self.click(self.fine_select)

    #选中配置的产品
    def click_product_name(self):
        self.click(self.product_location)

    def click_after_say(self):
        self.click(self.Afrer_say)
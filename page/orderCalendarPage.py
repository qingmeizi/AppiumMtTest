#选择套餐选择日期
from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction


class OrderCalendarPage(BaseAction):

   #选择套餐
    set_meal = By.XPATH, "//*[@text='测试套餐']"
   #选择日期
    select_data = By.XPATH,"//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[31]/android.view.ViewGroup"
   #选择场次
    select_session = By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"
   #设置出行人数+1


    travel_number = By.XPATH,"//android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView[2]"
   #点击确定
    determine_button = By.XPATH,"//*[@text='确定']"


    def __init__(self, driver):
        self.driver = driver

   #选择套餐
    def click_set_meal(self):
        self.click(self.set_meal)
    #选择日期
    def click_select_data(self):
        self.click(self.select_data)

    #选择场次
    def click_selech_session(self):
        self.click(self.select_session)

    #设置出行人数
    def click_travel_number(self):
        self.click(self.travel_number)
    #点击确定
    def click_determine_button(self):
        self.click(self.determine_button )




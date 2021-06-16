from selenium.webdriver.common.by import By
import os, sys
sys.path.append(os.getcwd())
from base.BaseAction import BaseAction

class SearchPage(BaseAction):

    #搜索页的搜索框
    search_input = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.EditText"
    #搜索按钮
    search_button = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]"
    #搜索列表选择第一个产品
    first_product = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup"
    activtiy_contant = "l"
    def __init__(self, driver):
        self.driver = driver

    def activity_contant_input(self):
        self.input(self.search_input,self.activtiy_contant)
    #点击搜索
    def click_search_button(self):
        self.click(self.search_button)
    #点击第一个产品
    def click_first_product(self):
        self.click(self.first_product)




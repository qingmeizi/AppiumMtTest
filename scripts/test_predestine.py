#预定
import os,sys
sys.path.append(os.getcwd())
import pytest
from appium import webdriver
from base.base_driver import init_driver
from page.beforHmoePage import BeforHomePage
from page.mainPage import MainHmoePage
from page.userHomePage import UserHmoePage
from page.userLoginPage import UserLoginPage
from page.detailPage import DetailPage
from page.orderCalendarPage import OrderCalendarPage
from page.orderSecondPage import OrderSecondPage
from page.paysucessPage import PaysucessPage
from base.base_yml import open_with_file
import time

from base.base_yml import open_with_file

#数据驱动
def find_with_data(key):
    return open_with_file("data")[key]


#进入设置操作
class Test_Predestine:
    def setup(self):
        self.driver = init_driver()
        self.beforHmoe = BeforHomePage(self.driver)
        self.mainpage = MainHmoePage(self.driver)
        self.userHomePage = UserHmoePage(self.driver)
        self.userLoginPage = UserLoginPage(self.driver)
        self.detailPage = DetailPage(self.driver)
        self.orderCalendarPage = OrderCalendarPage(self.driver)
        self.oderSecondPage = OrderSecondPage(self.driver)
        self.paysucessPage = PaysucessPage(self.driver)



    #前置
    #@pytest.mark.skipif(True, reason="done")
    def test_prdestine_beforeHmoe(self):
        #点击同意
        self.beforHmoe.click_agreen_button()
        #点击我知道了
        self.beforHmoe.click_Iknow()
        #点击first我知道了
        self.beforHmoe.click_first_know()
        #点击sencond我知道了
        self.beforHmoe.click_second_know()

        #点击three我知道了
        self.beforHmoe.click_three_know()

        #点击允许
        self.beforHmoe.click_allow_button()

        #点击取消
        #self.beforHmoe.click_cancel_button()
        #点击选中城市
        self.beforHmoe.click_select_city()
        time.sleep(3)

        # 点击我的
        self.mainpage.click_my_tab()
        # 点击登录/注册
        self.userHomePage.click_login_registered()
        # 点击手机登录
        self.userLoginPage.click_mobile_login()
        # 输入手机号
        self.userLoginPage.mobile_input()
        # 输入验证码
        self.userLoginPage.password_input()
        # 勾选
        self.userLoginPage.click_check_box()
        # 点击提交
        self.userLoginPage.click_submit()
        #下次再说
        self.userLoginPage.click_Next()

        # 点击首页
        self.userHomePage.click_homePage_tab()
        # 点击精选
        self.mainpage.click_fine_select()
        # 点击产品
        self.mainpage.click_product_name()

        # 点击立即购买
        self.detailPage.click_immediately_buy()
        # 选择套餐
        self.orderCalendarPage.click_set_meal()
        # 选择日期
        self.orderCalendarPage.click_select_data()
        # 选择场次
        self.orderCalendarPage.click_selech_session()
        # 选择出行人数
        self.orderCalendarPage.click_travel_number()
        # 点击确定
        self.orderCalendarPage.click_determine_button()
        # 点击提交订单
        self.oderSecondPage.click_ordersecond_confirm()

        # 输入第一个支付密码
        self.oderSecondPage.one_password_box_input()
        # 输入第二个支付米啊吗
        self.oderSecondPage.two_password_box_input()
        # 输入第三个支付密码
        self.oderSecondPage.three_password_box_input()
        # 输入第四个支付密码
        self.oderSecondPage.foure_password_box_input()
        # 输入第五个密码
        self.oderSecondPage.five_password_box_input()
        # 输入第六个密码
        self.oderSecondPage.six_password_box_input()

        contexts = self.driver.contexts
        print(contexts)

        #切换到webview
        self.driver.switch_to.context(contexts[1])

        #获取当前的环境，看是否切换成功
        now = self.driver.current_context()
        print(now)

        #点击订单详情按钮
        self.paysucessPage.click_orderdetail_button()

        # 切回native
        self.driver.switch_to.context(contexts[0])

        # driver.switch_to.context("NATIVE_APP") # 这样也是可以的

        # 获取当前的环境，看是否切换成功
        now = self.driver.current_context()
        print(now)

        

    #登录
   # @pytest.mark.parametrize("content",find_with_data("userLogin"))
 #   def test_prdestine_login(self,content):
    def test_prdestine_login(self):
        # 点击我的
        self.mainpage.click_my_tab()
        # 点击登录/注册
        self.userHomePage.click_login_registered()
        # 点击手机登录
        self.userLoginPage.click_mobile_login()
        # 输入手机号
        self.userLoginPage.mobile_input()
        # 输入验证码
        self.userLoginPage.password_input()
        # 勾选
        self.userLoginPage.click_check_box()
        # 点击提交
        self.userLoginPage.click_submit()

    #首页
    def test_prdestine_main(self):
        #点击首页
        self.userHomePage.click_homePage_tab()
        #点击精选
        self.mainpage.click_fine_select()
        #点击产品
        self.mainpage.click_product_name()


    #购买下单
    def test_prdestine_order(self):
        #点击立即购买
        self.detailPage.click_immediately_buy()
        #选择套餐
        self.orderCalendarPage.click_set_meal()
        #选择日期
        self.orderCalendarPage.click_select_data()
        #选择场次
        self.orderCalendarPage.click_selech_session()
        #选择出行人数
        self.orderCalendarPage.click_travel_number()
        #点击确定
        self.orderCalendarPage.click_determine_button()
        #点击提交订单
        self.oderSecondPage.click_ordersecond_confirm()

    @pytest.mark.parametrize("content",find_with_data("input_password"))
    def test_input_password(self,content):
        #输入第一个支付密码
        self.oderSecondPage.one_password_box_input1(content[0])
        #输入第二个支付米啊吗
        self.oderSecondPage.two_password_box_input1(content[1])
        #输入第三个支付密码
        self.oderSecondPage.three_password_box_input1(content[2])
        #输入第四个支付密码
        self.oderSecondPage.foure_password_box_input1(content[3])
        #输入第五个密码
        self.oderSecondPage.five_password_box_input1(content[4])
        #输入第六个密码
        self.oderSecondPage.six_password_box_input1(content[5])

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
import time
from base.base_yml import yaml_data_with_file

from base.base_yml import open_with_file


def data_with_key(key):
    return yaml_data_with_file("data",key)


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




    @pytest.mark.parametrize("content",data_with_key("test_prdestine_msg"))
    def test_prdestine_msg(self,content):
        #点击同意
        self.beforHmoe.click_agreen_button()
        #点击我知道了
        self.beforHmoe.click_Iknow()
        time.sleep(2)
        #点击first我知道了
        self.beforHmoe.click_first_know()
        #点击sencond我知道了
        self.beforHmoe.click_second_know()
        #点击three我知道了
        self.beforHmoe.click_three_know()
        time.sleep(3)

        #仅使用期间允许
        self.beforHmoe.click_allow_during()

        time.sleep(3)
        #点击允许
        #self.beforHmoe.click_allow_button()

        #点击取消
        #self.beforHmoe.click_cancel_button()
        #点击选中城市
        self.beforHmoe.click_select_city()
        time.sleep(3)

        #发现新版本，取消
        self.mainpage.click_after_say()
        time.sleep(2)
        # 点击我的
        self.mainpage.click_my_tab()
        # 点击登录/注册
        self.userHomePage.click_login_registered()
        # 点击手机登录
        self.userLoginPage.click_mobile_login()
        time.sleep(2)
        # 输入手机号
        self.userLoginPage.mobile_input(content["mobile"])
        # 输入验证码
        self.userLoginPage.password_input(content["password"])
        # 勾选
        self.userLoginPage.click_check_box()
        # 点击提交
        self.userLoginPage.click_submit()
        time.sleep(1)

        # 下次再说
        self.userLoginPage.click_Next()

        # 点击首页
        self.userHomePage.click_homePage_tab()
        time.sleep(1)
        # 发现新版本，取消
        self.mainpage.click_after_say()
        time.sleep(2)

        # 点击精选
        self.mainpage.click_fine_select()

        # 点击产品
        self.mainpage.click_product_name()
        time.sleep(2)

        # 点击立即购买
        self.detailPage.click_immediately_buy()
        time.sleep(1)
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
        time.sleep(2)
        # 点击提交订单
        self.oderSecondPage.click_ordersecond_confirm()



        # 输入第一个支付密码
        self.oderSecondPage.one_password_box_input1(content["one_password"])
        # 输入第二个支付米啊吗
        self.oderSecondPage.two_password_box_input1(content["two_password"])
        # 输入第三个支付密码
        self.oderSecondPage.three_password_box_input1(content["three_password"])
        # 输入第四个支付密码
        self.oderSecondPage.foure_password_box_input1(content["foure_password"])
        # 输入第五个密码
        self.oderSecondPage.five_password_box_input1(content["five_password"])
        # 输入第六个密码
        self.oderSecondPage.six_password_box_input1(content["six_password"])


        contexts = self.driver.contexts

        print(contexts)
        #['NATIVE_APP', 'WEBVIEW_com.maitao.mtqzy', 'WEBVIEW_stetho_com.maitao.mtqzy']
        time.sleep(1)
        # 切换到webview
        self.driver.switch_to.context(contexts[1])


        time.sleep(7)

        # 获取当前的环境，看是否切换成功
        now = self.driver.current_context
        print(now)
        os.system('pkill -9 chromedriver')

        # 点击订单详情按钮
        self.paysucessPage.click_orderdetail_button()

        # 切回native
        self.driver.switch_to.context(contexts[0])

        # driver.switch_to.context("NATIVE_APP") # 这样也是可以的

        # 获取当前的环境，看是否切换成功
        now = self.driver.current_context()
        print(now)

    def teardown(self):
        self.driver.quit()


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
class BaseAction:

    def __init__(self,driver):
        self.driver = driver

    #封装点击操作
    def click(self,loc):
        self.find_element(loc).click()

    #封装输入操作
    def input(self,loc,text):
        self.find_element(loc).send_keys(text)


    #封装元素findelement
    #def find_element(self,loc):
     #   return self.find_element(loc[0])

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            # XPAYH处理方法
            value = self.make_xpath_with_feature(value)
        # 下面这个是加显示等待
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

    # 多元素定位如：driver.find_elements_by_xpath()
    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        # 下面这个是加显示等待
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_elements(by, value))

    # 以下是PXATH工具类简化
    def make_xpath_with_unit_feature(self, loc):
        
        #拼接xpath中间部分
        #:param loc:
        #:return:
        
        key_index = 0  # 下标0
        value_index = 1  # 下标1
        option_index = 2  # 下标2
        args = loc.split(",")
        featre = ""

        if len(args) == 2:
            featre = "@" + args[key_index] + "='" + args[value_index] + "'" + "and"
        elif len(args) == 3:
            if args[option_index] == "0":
                featre = "@" + args[key_index] + "='" + args[value_index] + "'" + "and"
            elif args[option_index] == "1":
                featre = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"
        return featre

    # xpath调用简单用法
    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        featre = ""
        # 判断是不是字符串
        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc
            featre = self.make_xpath_with_unit_feature(loc)  # loc字符串拼接
        else:
            # loc列表拼接
            for i in loc:
                featre += self.make_xpath_with_unit_feature(i)
        # 删掉尾巴and
        featre = featre.rstrip("and")
        loc = feature_start + featre + feature_end

        return loc


"""
使用方法与描述
//*[contains(@text,'设置')] #包含查询
//*[@text='设置']  #精确查找
//*[comtains(@text,'设置')and@index='30'and@自动='d9999']#列表and且
以后输入以下就可以了
"text,设置"
"text,设置，0"
"text,设置，1"
["text,设置","text,设置,1","text,设置,0"]
"""



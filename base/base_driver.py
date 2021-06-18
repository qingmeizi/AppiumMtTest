from appium import webdriver
#from selenium import webdriver
import time

def init_driver():
        caps = {}
        caps["platformName"] = "Android"
        caps["AUTOMATION_NAME"] = "Appium"
        # caps["platformVersion"] = "9.0.0"
        caps["deviceName"] = "192.168.56.107:5555"
        caps["appPackage"] = "com.maitao.mtqzy"
        caps["appActivity"] = "com.maitao.mtqzy.main.SplashActivity"
        caps["automationName"] = "UiAutomator2"
        #caps["automationName"] = "Selendroid"

        caps["newCommandTimeout"] = 5000
        #caps["noReset"] = True
        caps["androidPackage"] = "com.android.chrome"
        caps["chromeOptions"] = {'androidProcess': 'com.tencent.mm:tools'} #驱动H5自动化关键之一
        caps["chromedriverExecutable"] = "/usr/local/H5_chromedriver/chromedriver"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        return driver


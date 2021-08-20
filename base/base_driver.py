from appium import webdriver
#from selenium import webdriver
import time

def init_driver():
        caps = {}
        caps["platformName"] = "Android"
        caps["AUTOMATION_NAME"] = "Appium"
        # caps["platformVersion"] = "9.0.0"
        caps["deviceName"] = "SNHVB20611009683"
        caps["appPackage"] = "com.maitao.mtqzy"
        caps["appActivity"] = "com.maitao.mtqzy.main.SplashActivity"
        caps["automationName"] = "UiAutomator2"
        #caps["automationName"] = "Selendroid"

        caps["newCommandTimeout"] = 5000
        #caps["noReset"] = True
        caps["androidPackage"] = "com.android.chrome"
        caps["chromeOptions"] = {'androidProcess': 'com.maitao.mtqzy'} #驱动H5自动化关键之一
        #caps["chromeOptions"] = {'androidProcess': 'WEBVIEW_stetho_com.maitao.mtqzy'}

        caps["chromedriverExecutable"] = "/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"
        caps['recreateChromeDriverSessions'] = True


        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        return driver


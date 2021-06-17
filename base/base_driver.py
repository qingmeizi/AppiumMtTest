from selenium import webdriver


def init_driver():
        caps = {}
        caps["platformName"] = "Android"
        caps["AUTOMATION_NAME"] = "Appium"
        # caps["platformVersion"] = "9.0.0"
        caps["deviceName"] = "192.168.56.107:5555"
        caps["appPackage"] = "com.maitao.mtqzy"
        caps["appActivity"] = "com.maitao.mtqzy.main.SplashActivity"
        caps["automationName"] = "UiAutomator2"
        caps["newCommandTimeout"] = 5000
        #caps["noReset"] = True
        caps["androidPackage"] = "com.android.chrome"

        caps["chromedriverExecutable"] = "/usr/local/H5_chromedriver/chromedriver"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        return driver

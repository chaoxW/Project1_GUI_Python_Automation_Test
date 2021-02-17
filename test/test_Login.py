from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Lib.Pages.loginPage import loginPage
from Lib.Pages.homePage import homePage
from Config.config_file import config

class loginPageTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome("../Lib/chromedriver.exe")
        # add chrome driver to PATH
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()


    def test_01_loginTest_valid(self):
        driver = self.driver
        url = config.homePage
        driver.get(url)

        login = loginPage(driver)
        userName = config.userName
        passWord = config.passWord
        login.enter_userName(userName)
        login.enter_passWord(passWord)
        login.click_login()
        login.check_home_logo()

        homepage = homePage(driver)
        homepage.click_userMenu()
        homepage.click_logOut()
        time.sleep(1)

    def test_02_loginTest_invalid(self):
        driver = self.driver
        url = config.homePage
        driver.get(url)
        login = loginPage(driver)
        userName = config.userName
        login.enter_userName(userName)
        login.enter_passWord("1234")
        login.click_login()
        time.sleep(2)
        msg = login.check_invalid_login_message()
        self.assertEqual(msg,"We didn't recognize that email and/or password. Need help?","INVALID error message with invalid login")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/shuai.wang/PycharmProjects/loginPage/Report"))

from Lib.Locators.locators import locators

class homePage():
    def __init__(self, driver):
        self.driver = driver
        self.userMenu_xpath = locators.userMenu_xpath
        self.logOutLink_css_selector = locators.logOutLink_css_selector

    def click_userMenu(self):
        self.driver.find_element_by_xpath(self.userMenu_xpath).click()

    def click_logOut(self):
        driver = self.driver
        driver.find_element_by_css_selector(self.logOutLink_css_selector).click()

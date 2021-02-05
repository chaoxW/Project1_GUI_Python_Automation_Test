from Lib.Locators.locators import locators

class loginPage():
    def __init__(self,driver):
        self.driver = driver
        self.userName_textbox_id = locators.userName_textbox_id
        self.passWord_textbox_id = locators.passWord_textbox_id
        self.login_button_id = locators.login_button_id
        self.invalid_login_message = locators.login_error_message


    def enter_userName(self,userName):
        driver = self.driver
        driver.find_element_by_id(self.userName_textbox_id).clear()
        driver.find_element_by_id(self.userName_textbox_id).send_keys(userName)
        print("insert userName: " + userName + " pass")

    def enter_passWord(self,passWord):
        driver = self.driver
        driver.find_element_by_id(self.passWord_textbox_id).clear()
        driver.find_element_by_id(self.passWord_textbox_id).send_keys(passWord)
        print("Insert passWord: " + passWord + " pass")

    def click_login(self):
        driver = self.driver
        driver.find_element_by_id(self.login_button_id).click()
        print("click login button pass")

    def check_invalid_login_message(self):
        driver = self.driver
        msg = driver.find_element_by_class_name(self.invalid_login_message).text
        return msg
from selenium import webdriver
class loginpage:
    username_id = "Email"
    password_id = "Password"
    login_xpath = "//button[normalize-space()='Log in']"
    logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clicklogin(self, login):
        self.driver.find_element_by_xpath(self.login_xpath).click()

    def clicklogout(self, logout):
        self.driver.find_element_by_link_text()(self.logout_linktext).click()

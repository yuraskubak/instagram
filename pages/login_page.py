class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click
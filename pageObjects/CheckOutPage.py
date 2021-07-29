from selenium.webdriver.common.by import By


class CheckOutPage:
    checkout_success = (By.CSS_SELECTOR, "button.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def get_checkout(self):
        return self.driver.find_element(*CheckOutPage.checkout_success)
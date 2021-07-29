from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop'")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit_btn = (By.XPATH, "//input[@value='Submit']")
    submit_message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shop_element(self):
        self.driver.find_element(*HomePage.shop).click()
        shop_page = ShopPage(self.driver)
        return shop_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def get_submit_message(self):
        return self.driver.find_element(*HomePage.submit_message)
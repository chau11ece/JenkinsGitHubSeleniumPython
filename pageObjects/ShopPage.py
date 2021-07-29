from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class ShopPage:

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer= (By.CSS_SELECTOR, ".card-footer button")
    check_out = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def get_card_titles(self):
        return self.driver.find_elements(*ShopPage.card_title)

    def get_card_footers(self):
        return self.driver.find_elements(*ShopPage.card_footer)

    def check_out_element(self):
        self.driver.find_element(*ShopPage.check_out).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page


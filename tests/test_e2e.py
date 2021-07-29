from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from pageObjects.CheckOutPage import CheckOutPage


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        # go to page SHOP
        shop_page = homepage.shop_element()

        # get car titles on the page of SHOP
        log.info("Getting all the card titles")
        products_lst = shop_page.get_card_titles()

        index = 0
        for product in products_lst:
            prod_name = product.text
            # print(prod_name)
            log.info(prod_name)
            if prod_name == 'Blackberry':
                # add item into cart
                shop_page.get_card_footers()[index].click()
                # print(*shop_page.get_card_footers(), sep="\n")

            index += 1

        # go to page CHECKOUT
        check_out_page = shop_page.check_out_element()

        checkoutpage = CheckOutPage(self.driver)
        checkoutpage.get_checkout().click()

        log.info("Entering country name as lan")
        self.driver.find_element_by_id("country").send_keys("lan")
        self.verify_link_presence("Netherlands")
        self.driver.find_element_by_link_text("Netherlands").click()
        self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        success_text = self.driver.find_element_by_css_selector(".alert-success").text
        log.info("Text received from application is " + success_text)
        assert "Success! Thank you!" in success_text

        self.driver.get_screenshot_as_file("screen.png")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        name = home_page.get_name()
        name.send_keys(get_data["firstname"])
        log.info("firstname is " + get_data["firstname"])
        email = home_page.get_email()
        email.send_keys(get_data["email"])
        checkbox = home_page.get_checkbox()
        checkbox.click()
        self.select_option_by_text(home_page.get_gender(), get_data["gender"])
        home_page.get_submit_btn().click()
        alert_text = home_page.get_submit_message().text
        assert "Success" in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param

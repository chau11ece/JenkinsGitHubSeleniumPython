import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import inspect


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        # create logger
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to DEBUG
        file_handler = logging.FileHandler('logfile.log')
        file_handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        # add formatter to ch
        file_handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(file_handler)  # handler object

        # 'application' code
        # logger.debug('debug message')
        # logger.info('info message')
        # logger.warning('warn message')
        # logger.error('error message')
        # logger.critical('critical message')

        return logger

    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

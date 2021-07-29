import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

driver = None


# add cmd line option and provide the cmdopt through a fixture function:
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    base_url = "https://rahulshettyacademy.com/angularpractice/"
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path="D:\\WebDriver\\geckodriver.exe")
    elif browser == "chrome":
        chromedriver = "D:\\WebDriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
    elif browser == "IE":
        driver = webdriver.Ie("D:\\WebDriver\\msedgedriver.exe")
    else:
        pass

    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """:cvar
    """

    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            file_name = report.nodeid.replace("::", "_") + timestamp + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

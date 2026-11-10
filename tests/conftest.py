import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture
def browser(request):

    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        b_driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
        b_driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("plz set bzr name by '--browser' opt")

    yield b_driver


    b_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

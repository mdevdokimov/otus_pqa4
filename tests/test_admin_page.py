from selenium.webdriver.common.by import By

URL = "http://10.212.41.182:8081/administration"

def test_title(browser):
    browser.get(URL)
    assert browser.title == "PrestaShop (PrestaShop™)", "ошибка в тайтле"

def test_email(browser):
    browser.get(URL)
    browser.find_element(By.ID, "email")

def test_passwd(browser):
    browser.get(URL)
    browser.find_element(By.ID, "passwd")

def test_submit(browser):
    browser.get(URL)
    browser.find_element(By.ID, "submit_login")

def test_forgot(browser):
    browser.get(URL)
    browser.find_element(By.ID, "forgot-password-link")

from selenium.webdriver.common.by import By

URL = "http://10.212.41.182:8081/registration"

def test_title(browser):
    browser.get(URL)
    assert browser.title == "Registration", "ошибка в тайтле"

def test_filds(browser):
    browser.get(URL)
    browser.find_element(By.ID, "field-firstname")
    browser.find_element(By.ID, "field-lastname")
    browser.find_element(By.ID, "field-email")
    browser.find_element(By.ID, "field-password")

    num_of_genders = len(browser.find_elements(By.NAME, "id_gender"))
    assert num_of_genders == 2


def test_check_boxes(browser):
    browser.get(URL)
    browser.find_element(By.NAME, "optin")
    browser.find_element(By.NAME, "psgdpr")
    browser.find_element(By.NAME, "newsletter")
    browser.find_element(By.NAME, "customer_privacy")


def test_show_pass(browser):
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, '#customer-form > div > div.field-password-policy > div > div.col-md-6.js-input-column > div.input-group.js-parent-focus > span > button')

def test_submit(browser):
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, "#customer-form > footer > button")

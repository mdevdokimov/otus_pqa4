import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://10.212.41.182:8081/"

def test_title(browser):
    browser.get(URL)
    assert browser.title == "PrestaShop"

def test_sign_in(browser):
    browser.get(URL)
    browser.find_element(By.XPATH, "//a[normalize-space()='Sign in']")

def test_currency(browser):
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, "#_desktop_currency_selector button")

def test_popular(browser):
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, "section.featured-products")
    popular_products = browser.find_elements(By.CSS_SELECTOR, "section.featured-products div.products article.product-miniature")
    assert len(popular_products) > 0, "Список 'Popular Products' пуст, товары не найдены"

def test_copyright(browser):
    browser.get(URL)
    copyright = browser.find_element(By.XPATH, "//footer//a[contains(text(), 'Ecommerce software by PrestaShop')]")
    assert "2026" in copyright.text, "В копирайте указан неверный год"
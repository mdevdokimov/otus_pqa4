import re
from selenium.webdriver.common.by import By

URL = "http://10.212.41.182:8081/9-art"

def test_title(browser):
    browser.get(URL)
    assert browser.title == "Art", "ошибка в тайтле"

def test_left_menu(browser):
    browser.get(URL)
    browser.find_element(By.ID, "left-column")
    browser.find_element(By.ID, "search_filters_suppliers")
    browser.find_element(By.ID, "search_filters_brands")
    browser.find_element(By.ID, "search_filters_wrapper")
    browser.find_element(By.ID, "search_filter_controls")
    browser.find_element(By.ID, "search_filters")

def test_main_block(browser):
    browser.get(URL)
    browser.find_element(By.ID, "main")
    browser.find_element(By.ID, "js-product-list-top")
    browser.find_element(By.ID, "js-product-list")

def test_products(browser):
    browser.get(URL)
    count_of_articles = len(browser.find_elements(By.CSS_SELECTOR, 'article.product-miniature'))
    assert count_of_articles >= 1, "не найдено ни одного артикла"

def test_price(browser):
    browser.get(URL)
    elements = browser.find_elements(By.CSS_SELECTOR, "article.product-miniature span.price")
    assert len(elements) > 0, "не найдены ценники"

    for element in elements:
        match = re.search(r"[0-9.,]+", element.text)
        price = float(match.group(0))
        assert price > 0, "найден невалидный ценник"

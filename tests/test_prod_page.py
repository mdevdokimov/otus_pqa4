import re
from selenium.webdriver.common.by import By

URL = "http://10.212.41.182:8081/art/3-13-the-best-is-yet-to-come-framed-poster.html"

def test_title(browser):
    browser.get(URL)
    assert browser.title == "The best is yet to come' Framed poster", "ошибка в тайтле"

def test_descr(browser):
    browser.get(URL)
    descr = browser.find_element(By.CSS_SELECTOR, "#main h1")
    assert descr.text == "THE BEST IS YET TO COME' FRAMED POSTER"

def test_price(browser):
    browser.get(URL)
    element = browser.find_element(By.CSS_SELECTOR, ".current-price")
    match = re.search(r"[0-9.,]+", element.text)
    price = float(match.group(0))
    assert price > 0, "невалидный ценник"

def test_add_to_bin(browser):
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, "button.add-to-cart[type='submit']")
    browser.find_element(By.CSS_SELECTOR, ".wishlist-button-add")

def test_image(browser):
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, "img.js-qv-product-cover")

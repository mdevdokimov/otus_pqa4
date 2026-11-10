import re
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://10.212.41.182:8081"

def extract_price(price_text):
    match = re.search(r"[0-9.,]+", price_text)
    if not match:
        raise ValueError(f"Не удалось извлечь число из ценника: '{price_text}'")
    return float(match.group(0).replace(",", "."))

@pytest.mark.parametrize("page_path", [
    "/",
    "/9-art"
])

def test_currency_change_updates_prices(browser, page_path):
    browser.get(f"{URL}{page_path}")
    wait = WebDriverWait(browser, 10)

    currency_btn_locator = (By.XPATH, "//*[contains(@id, '_desktop_currency_selector')]//button")
    currency_btn = wait.until(EC.element_to_be_clickable(currency_btn_locator))

    target_currency = "EUR" if "USD" in currency_btn.text else "USD"
    expected_symbol = "€" if target_currency == "EUR" else "$"

    first_product_price_locator = (By.XPATH, "//article[contains(@data-id-product, '1')]//span[normalize-space(@aria-label)='Price']")
    initial_price_el = wait.until(EC.visibility_of_element_located(first_product_price_locator))
    
    old_text = initial_price_el.text.strip()
    old_value = extract_price(old_text)


    currency_btn.click()
    target_option_locator = (
        By.XPATH, 
        f"//*[contains(@id, '_desktop_currency_selector')]//ul[contains(@class, 'dropdown-menu')]//a[contains(text(), '{target_currency}')]"
    )
    target_option = wait.until(EC.element_to_be_clickable(target_option_locator))
    target_option.click()


    wait.until(EC.text_to_be_present_in_element(currency_btn_locator, target_currency))


    updated_price_el = wait.until(EC.visibility_of_element_located(first_product_price_locator))
    new_text = updated_price_el.text.strip()
    new_value = extract_price(new_text)

    assert expected_symbol in new_text, f"В новой цене '{new_text}' отсутствует символ '{expected_symbol}'"
    assert new_value != old_value, f"Ценник не обновился: было '{old_text}', стало '{new_text}'"

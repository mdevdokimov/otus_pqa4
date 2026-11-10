import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://10.212.41.182:8081"

def test_add_random_product_to_bin(browser):
    browser.get(URL)
    wait = WebDriverWait(browser, 10)

    products = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//article[contains(@class, 'product-miniature')]"))
        )
    random_product = random.choice(products)

    title_link = random_product.find_element(By.XPATH, ".//*[contains(@class, 'product-title')]/a")
    title_link.click()

    product_h1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-header h1, #main h1")))
    expected_product_name = product_h1.text.strip()

    print(expected_product_name)

    #для всратой кружки

    customization_fields = browser.find_elements(By.CSS_SELECTOR, ".product-customization textarea, .product-customization input[type='text']")
    if len(customization_fields) > 0:
        for field in customization_fields:
            if field.is_displayed():
                field.clear()
                field.send_keys("TEEEEXT")

        save_custom_btn = browser.find_element(By.CSS_SELECTOR, "button[name='submitCustomizedData']")
        save_custom_btn.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".customization-message")))


    add_to_bin_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart[type='submit']"))
    )
    add_to_bin_btn.click()


    proceed_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='blockcart-modal']//a[contains(@href, 'cart')]"))
    )
    proceed_btn.click()


    bin_items = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-items .product-line-info a.label"))
    )
    bin_product_names = [item.text.strip() for item in bin_items]

    assert any(expected_product_name.lower() in name.lower() for name in bin_product_names), f"Товар '{expected_product_name}' не найден в корзине"
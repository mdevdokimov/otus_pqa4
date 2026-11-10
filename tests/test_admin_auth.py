from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://10.212.41.182:8081/administration"
ADM_LOGIN = "admin@example.com"
ADM_PASS = "Admin123!"

def test_admin_login_logout(browser):
    browser.get(URL)
    wait = WebDriverWait(browser, 10)
    assert browser.title == "PrestaShop (PrestaShop™)", "ошибка в тайтле"

    #логин

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys(ADM_LOGIN)

    password_input = browser.find_element(By.ID, "passwd")
    password_input.send_keys(ADM_PASS)

    submit = browser.find_element(By.ID, "submit_login")
    submit.click()

    sidebar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.nav-bar, #nav-sidebar")))
    assert sidebar.is_displayed(), "Не удалось войти в админку"

    #логоут

    profile_menu = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#header_infos #employee_infos, .employee-avatar, #header-employee-container .dropdown-toggle"))
    )
    profile_menu.click()

    logout = wait.until(EC.element_to_be_clickable((By.ID, "header_logout")))
    logout.click()


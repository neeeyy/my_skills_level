from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def web_wait(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )

@pytest.fixture
def browser():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        yield browser
    finally:
        browser.quit()

link = 'https://zdravcity.ru/r_spb/'

@pytest.mark.parametrize('phone', [
                             "9061235712"
                         ])

@pytest.mark.valid_apteka
def test_valid_phone(browser, phone):
        browser.get(link)
        profile_but = web_wait(browser, (By.CSS_SELECTOR, '[aria-label="Профиль"]'))
        profile_but.click()
        phone_input = web_wait(browser, (By.CSS_SELECTOR, '[placeholder="Введите номер телефона"]'))
        phone_input.click()
        phone_input.send_keys(phone)
        phone_input.send_keys('\t')
        sms_but = browser.find_element(By.XPATH, '//button[contains(text(), "Получить СМС-код")]')
        assert sms_but.is_enabled(), 'номер не подошел'
        assert "СМС" in sms_but.text, 'смс нет в тексте'

@pytest.mark.parametrize('phone', [
                             ("123"),
                             ("124325")
                         ])

@pytest.mark.nevalid_apteka
def test_nevalid_phone(browser, phone):
        browser.get(link)
        profile_but = web_wait(browser, (By.CSS_SELECTOR, '[aria-label="Профиль"]')).click()
        phone_input = web_wait(browser, (By.CSS_SELECTOR, '[placeholder="Введите номер телефона"]'))
        phone_input.click()
        phone_input.send_keys(phone)
        phone_input.send_keys('\t')
        sms_but = browser.find_element(By.XPATH, '//button[contains(text(), "Получить СМС-код")]')
        assert not sms_but.is_enabled()
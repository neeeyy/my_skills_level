import pytest
from selenium import webdriver
from phone_page import PhonePage
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize('phone', [
    '9061232332'
])

@pytest.mark.valid_test
def test_phone(browser, phone):
    page = PhonePage(browser)
    page.open('https://zdravcity.ru/r_spb/')
    page.open_profile()
    page.phone_number(phone)
    button = page.button()
    assert button.is_enabled()
    assert "СМС" in button.text

@pytest.mark.parametrize('phone', [
    '123',
    '1234'
])

@pytest.mark.invalid_test
def test_phone_number(browser, phone):
    page = PhonePage(browser)
    page.open('https://zdravcity.ru/r_spb/')
    page.open_profile()
    page.phone_number(phone)
    button = page.button()
    assert not button.is_enabled()

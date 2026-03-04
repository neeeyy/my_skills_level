from Base_class import BasePage
from selenium.webdriver.common.by import By


class PhonePage(BasePage):

    def open_profile(self):
        self.wait_web((By.CSS_SELECTOR, '[aria-label="Профиль"]')).click()

    def phone_number(self, phone):
        self.wait_web((By.CSS_SELECTOR, '[placeholder="Введите номер телефона"]')).send_keys(phone)

    def button(self):
        return self.wait_presence((By.XPATH, '//button[contains(text(), "Получить СМС-код")]'))


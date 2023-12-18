from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_Contact_CLICK = (By.CSS_SELECTOR, '''nav > ul > li:nth-child(2) > a''')
    LOCATOR_ENTER_NAME = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_ENTER_EMAIL = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_ENTER_TEXT = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    LOCATOR_CONTACT_US_CLICK = (By.CSS_SELECTOR, '''#contact > div.submit > button > span''')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def Contact_click(self):
        logging.info("Contact_click")
        self.find_element(TestSearchLocators.LOCATOR_Contact_CLICK).click()

    def enter_name(self, word):
        logging.info(f" {word} of element {TestSearchLocators.LOCATOR_ENTER_NAME[1]}")
        enter_name = self.find_element(TestSearchLocators.LOCATOR_ENTER_NAME)
        enter_name.clear()
        enter_name.send_keys(word)

    def enter_email(self, word):
        logging.info(f" {word} of element {TestSearchLocators.LOCATOR_ENTER_EMAIL[1]}")
        enter_email = self.find_element(TestSearchLocators.LOCATOR_ENTER_EMAIL)
        enter_email.clear()
        enter_email.send_keys(word)

    def enter_text(self, word):
        logging.info(f" {word} of element {TestSearchLocators.LOCATOR_ENTER_TEXT[1]}")
        enter_text = self.find_element(TestSearchLocators.LOCATOR_ENTER_TEXT)
        enter_text.clear()
        enter_text.send_keys(word)

    def click_contact_us(self):
        logging.info("click_contact_us")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_CLICK).click()

    def switch_alert(self):
        time.sleep(1)
        logging.info("Switch alert")
        alert = self.driver.switch_to.alert()
        logging.info(alert)
        return alert

    def get_alert_message(self):
        time.sleep(1)
        logging.info("Get alert message")
        txt = self.get_alert_txt()
        logging.info(f"Alert message is {txt}")
        return txt

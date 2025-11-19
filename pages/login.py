#login class
from selenium.webdriver.common.by import By
import time
import pytest

class TestSauceDemoLogin:
    USER_NAME_LOCATOR="input[name='user-name']"
    PASSWORD_LOCATOR="input[name='password']"
    LOGIN_BUTTON_LOCATOR="input[name='login-button']"


    def __init__(self):
        pass

    def login(self, driver,username,password):
        driver.find_element(By.CSS_SELECTOR,self.USER_NAME_LOCATOR).send_keys(username)
        driver.find_element(By.CSS_SELECTOR,self.PASSWORD_LOCATOR).send_keys(password)
        driver.find_element(By.CSS_SELECTOR,self.LOGIN_BUTTON_LOCATOR).click()
        time.sleep(2)
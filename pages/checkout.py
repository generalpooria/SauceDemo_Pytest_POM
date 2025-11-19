from selenium.webdriver.common.by import By
import time
import pytest



class CheckoutPage:
    CHECKOUT_BUTTON_SELECTOR = "button[id='checkout']"
    FIRST_NAME_SELECTOR = "input[id='first-name']"
    LAST_NAME_SELECTOR = "input[id='last-name']"
    POSTAL_CODE_SELECTOR = "input[id='postal-code']"
    CONTINUE_BUTTON_SELECTOR = "input[type='submit'][id='continue']"
    CHECKOUT_HEADER_SELECTOR = "span[class='title']"

    def __init__(self):
        pass

    def click_checkout(self, driver):
        driver.find_element(By.CSS_SELECTOR,self.CHECKOUT_BUTTON_SELECTOR).click()
        time.sleep(2)
    
    def verify_checkout_page(self, driver):
        checkout_header=driver.find_element(By.CSS_SELECTOR,self.CHECKOUT_HEADER_SELECTOR).text
        assert checkout_header=="Checkout: Your Information", "Not on checkout page"

    def fill_checkout_info(self, driver, first_name, last_name, postal_code):
        driver.find_element(By.CSS_SELECTOR,self.FIRST_NAME_SELECTOR).send_keys(first_name)
        driver.find_element(By.CSS_SELECTOR,self.LAST_NAME_SELECTOR).send_keys(last_name)
        driver.find_element(By.CSS_SELECTOR,self.POSTAL_CODE_SELECTOR).send_keys(postal_code)
        driver.find_element(By.CSS_SELECTOR,self.CONTINUE_BUTTON_SELECTOR).click()
        time.sleep(2)

    def go_to_overview(self, driver):
        driver.find_element(By.CSS_SELECTOR,self.CONTINUE_BUTTON_SELECTOR).click()
        time.sleep(2)
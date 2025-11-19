from selenium.webdriver.common.by import By
import time
import pytest

class TestAddToCart:
    DIVS_SELECTOR = "div[class='inventory_item_description']"
    ITEM_NAME_SELECTOR = " div a"
    BUTTON_SELECTOR = "button"
    CARD_COUNT_SELECTOR = "div a span"
    GO_TO_CART_SELECTOR = "div a[class*='cart']"

    def __init__(self):
        pass

    def add_item_to_cart(self, driver, item_name):
        divs = driver.find_elements(By.CSS_SELECTOR,self.DIVS_SELECTOR)
        item_names = []
        for div in divs:
            item=div.find_element(By.CSS_SELECTOR,self.ITEM_NAME_SELECTOR).text
            item_names.append(item)
        #search for specific item and add to cart
        for div in divs:
            item=div.find_element(By.CSS_SELECTOR,self.ITEM_NAME_SELECTOR).text
            if item_name==item:
                div.find_element(By.CSS_SELECTOR,self.BUTTON_SELECTOR).click()
                break

    def check_item_in_cart(self, driver, item_name):
        cart_count=driver.find_element(By.CSS_SELECTOR,self.CARD_COUNT_SELECTOR).text
        assert cart_count=="1", "Item not added to cart"
    def go_to_cart(self, driver):
        driver.find_element(By.CSS_SELECTOR,self.GO_TO_CART_SELECTOR).click()
        time.sleep(2)
    
    def verify_item_in_cart(self, driver, item_name):
        item_in_cart=driver.find_element(By.CSS_SELECTOR,".cart_item div a").text
        assert item_in_cart==item_name, "Wrong item in cart"
        print("Correct item in cart:", item_in_cart)
from selenium.webdriver.common.by import By
import time
import pytest


class OverviewPage:
    OVERVIEW_HEADER_SELECTOR = "span[class='title']"

    def __init__(self):
        pass

    def verify_overview_page(self, driver):
        overview_header=driver.find_element(By.CSS_SELECTOR,self.OVERVIEW_HEADER_SELECTOR).text
        assert overview_header=="Checkout: Overview", "Not on overview page"
        print("Overview page verified:", overview_header)
        time.sleep(2)
    
    def finish_checkout(self, driver):
        driver.find_element(By.CSS_SELECTOR,"[class='btn btn_action btn_medium cart_button']").click()
        time.sleep(2)

    def verify_order_complete(self, driver):
        complete_header=driver.find_element(By.CSS_SELECTOR,"[class='complete-header']").text
        assert complete_header=="Thank you for your order!", "Order not complete"
        print("Order complete:", complete_header)
        #take screenshot
        driver.save_screenshot("order_complete.png")
        time.sleep(2)

  
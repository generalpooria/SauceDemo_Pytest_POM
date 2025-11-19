#impost selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import pytest
from pages.login import TestSauceDemoLogin
from pages.add_to_cart import TestAddToCart
from pages.checkout import CheckoutPage
from pages.overview import OverviewPage

class TestSauceDemoPurchase:
    def test_complete_purchase_flow(self, driver: WebDriver, test_data: dict):

        # Extract data from the fixture
        login_creds = test_data["login_credentials"]
        product_info = test_data["product"]
        checkout_details = test_data["checkout_info"]

        #login
        TestSauceDemoLogin().login(driver, login_creds["username"], login_creds["password"])

        #add to cart
        item_to_add = product_info["item_name"]
        TestAddToCart().add_item_to_cart(driver, item_to_add)

        #check if added (div a span)
        TestAddToCart().check_item_in_cart(driver, item_to_add)

        #go to cart
        TestAddToCart().go_to_cart(driver)

        #verify item in cart
        TestAddToCart().verify_item_in_cart(driver, item_to_add)

        #checkout
        CheckoutPage().click_checkout(driver)

        #verify checkout page
        CheckoutPage().verify_checkout_page(driver)

        #fill in checkout info
        CheckoutPage().fill_checkout_info(
            driver, 
            checkout_details["first_name"], 
            checkout_details["last_name"], 
            checkout_details["postal_code"]
        )
    
        #verify overview page
        OverviewPage().verify_overview_page(driver)

        #finish checkout
        OverviewPage().finish_checkout(driver)

        #verify order complete
        OverviewPage().verify_order_complete(driver)
        